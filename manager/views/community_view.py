from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from base.views import AjaxableResponseMixin
from manager.models import Community, Collection, Publication

class CommunityListView(ListView):
	template_name = 'manager/community/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = Community.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Community.objects.filter(** kwargs)
		return Community.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(CommunityListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:community_list", kwargs={"page":1})
		return context

class CommunityCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/community/form.html'
	model = Community
	fields = ['name','acronym']
	success_url = reverse_lazy('manager:community_list', kwargs={'page': 1})

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
		return Collection.objects.filter(communities=self.object.id)

class CommunityPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/community/publications.html'
	fields_search = Publication.FIELDS_SEARCH

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Community.objects.all())
		return super(CommunityPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(CommunityPublicationsView, self).get_context_data( ** kwargs)
		context['community'] = self.object
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:community_publications", kwargs={"slug":self.object.slug, "page":1})
		return context

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		collections = Collection.objects.filter(communities=self.object.id)
		publications = []
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			for collection in collections:
				temp_publications = Publication.objects.filter(is_final=True, collection=collection.id, ** kwargs)
				for publication in temp_publications:
					publications.append(publication)
		else:
			for collection in collections:
				temp_publications = Publication.objects.filter(is_final=True, collection=collection.id)
				for publication in temp_publications:
					publications.append(publication)
		return publications