from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Subject

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required, permission_required
#@method_decorator(permission_required, 'manager.admin_subject_list')

class SubjectListView(ListView):
	template_name = 'manager/admin/subject/list.html'
	paginate_by = settings.PAGINATE_BY
	queryset = Subject.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(SubjectListView, self).get_context_data( ** kwargs)
		return context

class SubjectCreateView(CreateView):
	template_name = 'manager/admin/subject/form.html'
	model = Subject
	fields = ['name']
	success_url = reverse_lazy('manager:admin_subject_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(SubjectCreateView, self).form_valid(form)

class SubjectUpdateView(UpdateView):
	template_name = 'manager/admin/subject/form.html'
	model = Subject
	fields = ['name',]
	success_url = reverse_lazy('manager:admin_subject_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(SubjectUpdateView, self).form_valid(form)

class SubjectDeleteView(DeleteView):
	template_name = 'manager/admin/subject/check_delete.html'
	model = Subject
	success_url = reverse_lazy('manager:admin_subject_list', kwargs={'page': 1})

class SubjectDetailView(DetailView):
	template_name = 'manager/admin/subject/detail.html'
	model = Subject

	def get_context_data(self, ** kwargs):
		context = super(SubjectDetailView, self).get_context_data( ** kwargs)
		return context