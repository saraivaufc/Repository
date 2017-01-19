from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.contrib import messages

from base.views import AjaxableResponseMixin, CSVResponseMixin, SearchResponseMixin
from manager.models import Keyword, Publication
from manager.utils.constants import Constants as ConstantsManager

class KeywordListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/keyword/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Keyword

class KeywordCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/keyword/form.html'
	model = Keyword
	fields = ['name']
	success_url = reverse_lazy('manager:keyword_list')

class KeywordUpdateView(UpdateView):
	template_name = 'manager/keyword/form.html'
	model = Keyword
	fields = ['name',]
	success_url = reverse_lazy('manager:keyword_list')
	
	def form_valid(self, form):
		messages.success(self.request, ConstantsManager.KEYWORD_SUCCESS_CHANGED)
		return super(KeywordUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, ConstantsManager.KEYWORD_ERROR_CHANGED)
		return super(KeywordUpdateView, self).form_invalid(form)

class KeywordDeleteView(DeleteView):
	template_name = 'manager/keyword/check_delete.html'
	model = Keyword
	success_url = reverse_lazy('manager:keyword_list')

class KeywordDetailView(DetailView):
	template_name = 'manager/keyword/detail.html'
	model = Keyword

	def get_context_data(self, ** kwargs):
		context = super(KeywordDetailView, self).get_context_data( ** kwargs)
		return context

class KeywordPublicationsView(SearchResponseMixin, SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/keyword/publications.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Keyword.objects.all())
		return super(KeywordPublicationsView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		queryset = super(KeywordPublicationsView, self).get_queryset()
		principal_keywords = queryset.filter(principal_keywords=self.object, is_final=True)
		secondary_keywords = queryset.filter(secondary_keywords=self.object, is_final=True)
		return list(principal_keywords) + list(secondary_keywords)