from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from manager.models import Subject, Publication
from manager.models import publication
from manager.models import subject

class SubjectListView(ListView):
	template_name = 'manager/subject/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = subject.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Subject.objects.filter(** kwargs)
		return Subject.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(SubjectListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:subject_list", kwargs={"page":1})
		return context

class SubjectCreateView(CreateView):
	template_name = 'manager/subject/form.html'
	model = Subject
	fields = ['name']
	success_url = reverse_lazy('manager:subject_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(SubjectCreateView, self).form_valid(form)

class SubjectUpdateView(UpdateView):
	template_name = 'manager/subject/form.html'
	model = Subject
	fields = ['name',]
	success_url = reverse_lazy('manager:subject_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(SubjectUpdateView, self).form_valid(form)

class SubjectDeleteView(DeleteView):
	template_name = 'manager/subject/check_delete.html'
	model = Subject
	success_url = reverse_lazy('manager:subject_list', kwargs={'page': 1})

class SubjectDetailView(DetailView):
	template_name = 'manager/subject/detail.html'
	model = Subject

	def get_context_data(self, ** kwargs):
		context = super(SubjectDetailView, self).get_context_data( ** kwargs)
		return context

class SubjectPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/subject/publications.html'
	fields_search = publication.FIELDS_SEARCH

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Subject.objects.all())
		return super(SubjectPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(SubjectPublicationsView, self).get_context_data( ** kwargs)
		context['subject'] = self.object
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:subject_publications", kwargs={"slug":self.object.slug, "page":1})
		return context

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publication.objects.filter(is_final=True, subjects=self.object.id, ** kwargs)
		return Publication.objects.filter(is_final=True, subjects=self.object.id)