from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Keyword, Publication
from manager.models import publication
from manager.models import keyword

class KeywordListView(ListView):
	template_name = 'manager/keyword/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = keyword.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Keyword.objects.filter(** kwargs)
		return Keyword.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(KeywordListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:keyword_list", kwargs={"page":1})
		return context

class KeywordCreateView(CreateView):
	template_name = 'manager/keyword/form.html'
	model = Keyword
	fields = ['name']
	success_url = reverse_lazy('manager:keyword_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(KeywordCreateView, self).form_valid(form)

class KeywordUpdateView(UpdateView):
	template_name = 'manager/keyword/form.html'
	model = Keyword
	fields = ['name',]
	success_url = reverse_lazy('manager:keyword_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(KeywordUpdateView, self).form_valid(form)

class KeywordDeleteView(DeleteView):
	template_name = 'manager/keyword/check_delete.html'
	model = Keyword
	success_url = reverse_lazy('manager:keyword_list', kwargs={'page': 1})

class KeywordDetailView(DetailView):
	template_name = 'manager/keyword/detail.html'
	model = Keyword

	def get_context_data(self, ** kwargs):
		context = super(KeywordDetailView, self).get_context_data( ** kwargs)
		return context

class KeywordPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/keyword/publications.html'
	fields_search = publication.FIELDS_SEARCH

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Keyword.objects.all())
		return super(KeywordPublicationsView, self).get(request, * args, ** kwargs)
	
	def get_context_data(self, ** kwargs):
		context = super(KeywordPublicationsView, self).get_context_data( ** kwargs)
		context['keyword'] = self.object
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:keyword_publications", kwargs={"slug":self.object.slug, "page":1})
		return context

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publication.objects.filter(is_final=True, keywords=self.object.id, ** kwargs)
		return Publication.objects.filter(is_final=True, keywords=self.object.id)