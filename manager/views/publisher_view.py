from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from base.views import AjaxableResponseMixin, SearchResponseMixin, CSVResponseMixin
from manager.models import Publisher, Publication

class PublisherListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'manager/publisher/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Publisher

class PublisherCreateView(AjaxableResponseMixin, CreateView):
	template_name = 'manager/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:publisher_list')

class PublisherUpdateView(UpdateView):
	template_name = 'manager/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:publisher_list')
	
	def form_valid(self, form):
		return super(PublisherUpdateView, self).form_valid(form)

class PublisherDeleteView(DeleteView):
	template_name = 'manager/publisher/check_delete.html'
	model = Publisher
	success_url = reverse_lazy('manager:publisher_list')

class PublisherDetailView(DetailView):
	template_name = 'manager/publisher/detail.html'
	model = Publisher

	def get_context_data(self, ** kwargs):
		context = super(PublisherDetailView, self).get_context_data( ** kwargs)
		return context

class PublisherPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/publisher/publications.html'
	model = Publication

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Publisher.objects.all())
		return super(PublisherPublicationsView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		queryset = super(PublisherPublicationsView, self).get_queryset()
		return queryset.filter(publisher=self.object, is_final=True)