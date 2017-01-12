from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from base.views import AjaxableResponseMixin, SearchResponseMixin, CSVResponseMixin
from manager.models import Subject, Publication

class SubjectListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/subject/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Subject

class SubjectCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/subject/form.html'
	model = Subject
	fields = ['name']
	success_url = reverse_lazy('manager:subject_list')

class SubjectUpdateView(UpdateView):
	template_name = 'manager/subject/form.html'
	model = Subject
	fields = ['name',]
	success_url = reverse_lazy('manager:subject_list')
	
	def form_valid(self, form):
		return super(SubjectUpdateView, self).form_valid(form)

class SubjectDeleteView(DeleteView):
	template_name = 'manager/subject/check_delete.html'
	model = Subject
	success_url = reverse_lazy('manager:subject_list')

class SubjectDetailView(DetailView):
	template_name = 'manager/subject/detail.html'
	model = Subject

	def get_context_data(self, ** kwargs):
		context = super(SubjectDetailView, self).get_context_data( ** kwargs)
		return context

class SubjectPublicationsView(SearchResponseMixin, SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/subject/publications.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Subject.objects.all())
		return super(SubjectPublicationsView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		queryset = super(SubjectPublicationsView, self).get_queryset()
		return queryset.filter(subjects=self.object, is_final=True)