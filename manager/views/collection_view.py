from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from base.views import AjaxableResponseMixin, SearchResponseMixin, CSVResponseMixin
from manager.models import Collection, Publication

class CollectionListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/collection/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Collection

class CollectionCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/collection/form.html'
	model = Collection
	fields = ['communities','name', 'description']
	success_url = reverse_lazy('manager:collection_list')

	def form_valid(self, form):
		return super(CollectionCreateView, self).form_valid(form)

class CollectionUpdateView(UpdateView):
	template_name = 'manager/collection/form.html'
	model = Collection
	fields = ['communities','name', 'description']
	success_url = reverse_lazy('manager:collection_list')
	
	def form_valid(self, form):
		return super(CollectionUpdateView, self).form_valid(form)

class CollectionDeleteView(DeleteView):
	template_name = 'manager/collection/check_delete.html'
	model = Collection
	success_url = reverse_lazy('manager:collection_list')

class CollectionDetailView(DetailView):
	template_name = 'manager/collection/detail.html'
	model = Collection

	def get_context_data(self, ** kwargs):
		context = super(CollectionDetailView, self).get_context_data( ** kwargs)
		return context

class CollectionPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/collection/publications.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Collection.objects.all())
		return super(CollectionPublicationsView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		queryset = super(CollectionPublicationsView, self).get_queryset()
		return queryset.filter(collection=self.object, is_final=True)