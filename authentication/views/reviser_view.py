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

class ReviserListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'authentication/reviser/list.html'
	paginate_by = settings.PAGINATE_BY
	model = User

	def get_queryset(self):
		queryset = super(ReviserListView, self).get_queryset()
		return queryset.filter(is_reviser=True)

class ReviserCreateView(CreateView):
	template_name = 'authentication/reviser/form.html'
	model = User
	fields = ['email']

	def get_success_url(self):
		return reverse_lazy('authentication:reviser_list', kwargs={'page':1})

	def post(self, request, * args, ** kwargs):
		email = self.request.POST.get('email')
		group = Group.objects.get(name="reviser")
		for user in User.objects.filter(email=email):
			user.is_reviser=True
			user.groups.add(group)
			user.save()
			return HttpResponseRedirect(self.get_success_url())
		return super(ReviserCreateView, self).post(request, * args, ** kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_reviser=True
		user.set_password(user.email)
		user.save(group="reviser")
		return super(ReviserCreateView, self).form_valid(form)

class ReviserDeleteView(DeleteView):
	template_name = 'authentication/reviser/check_delete.html'
	model = User
	success_url = reverse_lazy('authentication:reviser_list', kwargs={'page': 1})

	def post(self, request, * args, ** kwargs):
		group = Group.objects.get(name="reviser")
		for user in User.objects.filter(pk=self.get_object().pk):
			user.is_reviser=False
			user.groups.remove(group)
			user.save()
		return HttpResponseRedirect(self.success_url)