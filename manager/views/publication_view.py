from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
import hashlib

from base.views import AjaxableResponseMixin, SearchResponseMixin, CSVResponseMixin
from manager.models import Publication

class PublicationListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/publication/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Publication

	def get_queryset(self):
		queryset = super(PublicationListView, self).get_queryset()
		return queryset.filter(is_final=True)

class PublicationCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/publication/form.html'
	model = Publication
	fields = ['title', 'typology', 'subjects', 'authors', 'community',
			  'collection', 'publisher', 'address', 'year', 'reference',
			  'principal_language', 'principal_abstract', 'principal_keywords', 
			  'secondary_language', 'secondary_abstract', 'secondary_keywords', 
			  'issue_date', 'file']
	success_url = reverse_lazy('manager:publication_list')

	def form_valid(self, form):
		form.instance.is_final=True
		return super(PublicationCreateView, self).form_valid(form)

class PublicationUpdateView(UpdateView):
	template_name = 'manager/publication/form.html'
	model = Publication
	fields = ['title', 'typology', 'subjects', 'authors', 'community',
			  'collection', 'publisher', 'address', 'year', 'reference',
			  'principal_language', 'principal_abstract', 'principal_keywords', 
			  'secondary_language', 'secondary_abstract', 'secondary_keywords', 
			  'issue_date', 'file']
	success_url = reverse_lazy('manager:publication_list')
	
	def form_valid(self, form):
		form.instance.is_final=True
		return super(PublicationUpdateView, self).form_valid(form)

class PublicationDeleteView(DeleteView):
	template_name = 'manager/publication/check_delete.html'
	model = Publication
	success_url = reverse_lazy('manager:publication_list')

class PublicationDetailView(DetailView):
	template_name = 'manager/publication/detail.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		if not self.get_object().is_final:
			return HttpResponseRedirect(reverse_lazy('manager:publication_list'))
		return super(PublicationDetailView, self).get(request, * args, ** kwargs)

	def get_context_data(self, ** kwargs):
		context = super(PublicationDetailView, self).get_context_data( ** kwargs)
		return context