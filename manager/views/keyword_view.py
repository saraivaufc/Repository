from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Keyword, Publication

class KeywordListView(ListView):
	template_name = 'manager/keyword/list.html'
	paginate_by = settings.PAGINATE_BY
	queryset = Keyword.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(KeywordListView, self).get_context_data( ** kwargs)
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

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Keyword.objects.all())
		return super(KeywordPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(KeywordPublicationsView, self).get_context_data( ** kwargs)
		context['keyword'] = self.object
		return context
	def get_queryset(self):
		return Publication.objects.filter(keywords=self.object.id)