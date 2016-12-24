from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
import hashlib

from manager.models import Publication
from manager.models import publication

class PublicationListView(ListView):
	template_name = 'manager/publication/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = publication.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publication.objects.filter(** kwargs)
		return Publication.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(PublicationListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:publication_list", kwargs={"page":1})
		return context

class PublicationCreateView(CreateView):
	template_name = 'manager/publication/form.html'
	model = Publication
	fields = ['title', 'typology', 'subjects', 'authors', 'advisors', 
			  'collection', 'publisher', 'address', 'year', 'reference','language', 
			  'abstract', 'other_abstract', 'keywords', 'issue_date', 'file']
	success_url = reverse_lazy('manager:publication_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(PublicationCreateView, self).form_valid(form)

class PublicationUpdateView(UpdateView):
	template_name = 'manager/publication/form.html'
	model = Publication
	fields = ['title', 'typology', 'subjects', 'authors', 'advisors', 
			  'collection', 'publisher', 'address', 'year', 'reference','language', 
			  'abstract', 'other_abstract', 'keywords', 'issue_date', 'file']
	success_url = reverse_lazy('manager:publication_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(PublicationUpdateView, self).form_valid(form)

class PublicationDeleteView(DeleteView):
	template_name = 'manager/publication/check_delete.html'
	model = Publication
	success_url = reverse_lazy('manager:publication_list', kwargs={'page': 1})

class PublicationDetailView(DetailView):
	template_name = 'manager/publication/detail.html'
	model = Publication

	def get_context_data(self, ** kwargs):
		context = super(PublicationDetailView, self).get_context_data( ** kwargs)
		return context