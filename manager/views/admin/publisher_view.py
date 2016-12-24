from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Publisher

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required, permission_required
#@method_decorator(permission_required, 'manager.admin_publisher_list')


class PublisherListView(ListView):
	template_name = 'manager/admin/publisher/list.html'
	paginate_by = settings.PAGINATE_BY
	queryset = Publisher.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(PublisherListView, self).get_context_data( ** kwargs)
		return context

class PublisherCreateView(CreateView):
	template_name = 'manager/admin/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:admin_publisher_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(PublisherCreateView, self).form_valid(form)

class PublisherUpdateView(UpdateView):
	template_name = 'manager/admin/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:admin_publisher_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(PublisherUpdateView, self).form_valid(form)

class PublisherDeleteView(DeleteView):
	template_name = 'manager/admin/publisher/check_delete.html'
	model = Publisher
	success_url = reverse_lazy('manager:admin_publisher_list', kwargs={'page': 1})

class PublisherDetailView(DetailView):
	template_name = 'manager/admin/publisher/detail.html'
	model = Publisher

	def get_context_data(self, ** kwargs):
		context = super(PublisherDetailView, self).get_context_data( ** kwargs)
		return context