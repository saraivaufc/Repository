from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group

from authentication.models import User, user

class ReviserListView(ListView):
	template_name = 'submission/reviser/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = user.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return User.objects.filter(is_reviser=True, ** kwargs)
		return User.objects.filter(is_reviser=True)

	def get_context_data(self, ** kwargs):
		context = super(ReviserListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("submission:reviser_list", kwargs={"page":1})
		return context

class ReviserCreateView(CreateView):
	template_name = 'submission/reviser/form.html'
	model = User
	fields = ['email']

	def get_success_url(self):
		return reverse_lazy('submission:reviser_list', kwargs={'page':1})

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
	template_name = 'submission/reviser/check_delete.html'
	model = User
	success_url = reverse_lazy('submission:reviser_list', kwargs={'page': 1})

	def post(self, request, * args, ** kwargs):
		group = Group.objects.get(name="reviser")
		for user in User.objects.filter(pk=self.get_object().pk):
			user.is_reviser=False
			user.groups.remove(group)
			user.save()
		return HttpResponseRedirect(self.success_url)