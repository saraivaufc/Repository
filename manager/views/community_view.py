from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Community, Collection, Publication

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required, permission_required
#@method_decorator(permission_required, 'manager.community_list')


class CommunityListView(ListView):
	template_name = 'manager/community/list.html'
	paginate_by = settings.PAGINATE_BY
	queryset = Community.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(CommunityListView, self).get_context_data( ** kwargs)
		return context

class CommunityCreateView(CreateView):
	template_name = 'manager/community/form.html'
	model = Community
	fields = ['name','acronym']
	success_url = reverse_lazy('manager:community_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(CommunityCreateView, self).form_valid(form)

class CommunityUpdateView(UpdateView):
	template_name = 'manager/community/form.html'
	model = Community
	fields = ['name','acronym']
	success_url = reverse_lazy('manager:community_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(CommunityUpdateView, self).form_valid(form)

class CommunityDeleteView(DeleteView):
	template_name = 'manager/community/check_delete.html'
	model = Community
	success_url = reverse_lazy('manager:community_list', kwargs={'page': 1})

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
		return Collection.objects.filter(community=self.object.id)

class CommunityPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/community/publications.html'

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Community.objects.all())
		return super(CommunityPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(CommunityPublicationsView, self).get_context_data( ** kwargs)
		context['community'] = self.object
		return context
	def get_queryset(self):
		collections = Collection.objects.filter(community=self.object.id)
		publications = []
		for collection in collections:
			temp_publications = Publication.objects.filter(collection=collection.id)
			for publication in temp_publications:
				publications.append(publication)
		return publications