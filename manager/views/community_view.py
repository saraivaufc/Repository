from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from base.views import AjaxableResponseMixin, SearchResponseMixin, CSVResponseMixin
from manager.models import Community, Collection, Publication

class CommunityListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/community/list.html'
	paginate_by = settings.PAGINATE_BY
	model =Community

class CommunityCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/community/form.html'
	model = Community
	fields = ['name','acronym']
	success_url = reverse_lazy('manager:community_list')

class CommunityUpdateView(UpdateView):
	template_name = 'manager/community/form.html'
	model = Community
	fields = ['name','acronym']
	success_url = reverse_lazy('manager:community_list')
	
	def form_valid(self, form):
		return super(CommunityUpdateView, self).form_valid(form)

class CommunityDeleteView(DeleteView):
	template_name = 'manager/community/check_delete.html'
	model = Community
	success_url = reverse_lazy('manager:community_list')

class CommunityDetailView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/community/detail.html'
	
	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Community.objects.all())
		return super(CommunityDetailView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(CommunityDetailView, self).get_context_data( ** kwargs)
		context['community'] = self.object
		return context
	def get_queryset(self):
		return Collection.objects.filter(communities=self.object.id)

class CommunityPublicationsView(SearchResponseMixin, SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/community/publications.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Community.objects.all())
		return super(CommunityPublicationsView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		queryset = super(CommunityPublicationsView, self).get_queryset()
		return queryset.filter(community=self.object, is_final=True)