from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group

from base.views import SearchResponseMixin, CSVResponseMixin
from authentication.models import User
from inbox.views import MessageSendView

class AdministratorListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'authentication/administrator/list.html'
	paginate_by = settings.PAGINATE_BY
	model = User

	def get_queryset(self):
		queryset = super(AdministratorListView, self).get_queryset()
		return queryset.filter(is_staff=True)
		
class AdministratorCreateView(CreateView):
	template_name = 'authentication/administrator/form.html'
	model = User
	fields = ['email']

	def get_success_url(self):
		return reverse_lazy('authentication:administrator_list')

	def post(self, request, * args, ** kwargs):
		email = self.request.POST.get('email')
		user = User.objects.filter(email=email).first()
		if not user:
			user = User(email=email)
			user.set_password(email)
			user.save()
		group = Group.objects.get(name="administrator")
		user.is_staff = True
		user.groups.add(group)
		user.save()
		MessageSendView.send_message(
			from_email=request.user.email,
			to_email=user.email,
			subject=_("Account"),
			message=_("You is Administrator!"),
		)
		return HttpResponseRedirect(self.get_success_url())

class AdministratorDeleteView(DeleteView):
	template_name = 'authentication/administrator/check_delete.html'
	model = User
	success_url = reverse_lazy('authentication:administrator_list')

	def post(self, request, * args, ** kwargs):
		group = Group.objects.get(name="administrator")
		for user in User.objects.filter(pk=self.get_object().pk):
			user.is_staff = False
			user.groups.remove(group)
			user.save()
		return HttpResponseRedirect(self.success_url)