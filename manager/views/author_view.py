from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Author, Publication

class AuthorListView(ListView):
	template_name = 'manager/author/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = Author.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Author.objects.filter(** kwargs)
		return Author.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(AuthorListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:author_list", kwargs={"page":1})
		return context

class AuthorCreateView(CreateView):
	template_name = 'manager/author/form.html'
	model = Author
	fields = ['first_name', 'last_name']
	success_url = reverse_lazy('manager:author_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(AuthorCreateView, self).form_valid(form)

class AuthorUpdateView(UpdateView):
	template_name = 'manager/author/form.html'
	model = Author
	fields = ['first_name', 'last_name']
	success_url = reverse_lazy('manager:author_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(AuthorUpdateView, self).form_valid(form)

class AuthorDeleteView(DeleteView):
	template_name = 'manager/author/check_delete.html'
	model = Author
	success_url = reverse_lazy('manager:author_list', kwargs={'page': 1})

class AuthorDetailView(DetailView):
	template_name = 'manager/author/detail.html'
	model = Author

	def get_context_data(self, ** kwargs):
		context = super(AuthorDetailView, self).get_context_data( ** kwargs)
		return context

class AuthorPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/author/publications.html'
	fields_search = Publication.FIELDS_SEARCH

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Author.objects.all())
		return super(AuthorPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(AuthorPublicationsView, self).get_context_data( ** kwargs)
		context['author'] = self.object
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:author_publications", kwargs={"slug":self.object.slug, "page":1})
		return context

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publication.objects.filter(is_final=True, authors=self.object.id, ** kwargs)
		return Publication.objects.filter(is_final=True, authors=self.object.id)