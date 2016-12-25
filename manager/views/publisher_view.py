from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Publisher, Publication
from manager.models import publication
from manager.models import publisher

class PublisherListView(ListView):
	template_name = 'manager/publisher/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = publisher.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publisher.objects.filter(** kwargs)
		return Publisher.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(PublisherListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:publisher_list", kwargs={"page":1})
		return context

class PublisherCreateView(CreateView):
	template_name = 'manager/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:publisher_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(PublisherCreateView, self).form_valid(form)

class PublisherUpdateView(UpdateView):
	template_name = 'manager/publisher/form.html'
	model = Publisher
	fields = ['name']
	success_url = reverse_lazy('manager:publisher_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(PublisherUpdateView, self).form_valid(form)

class PublisherDeleteView(DeleteView):
	template_name = 'manager/publisher/check_delete.html'
	model = Publisher
	success_url = reverse_lazy('manager:publisher_list', kwargs={'page': 1})

class PublisherDetailView(DetailView):
	template_name = 'manager/publisher/detail.html'
	model = Publisher

	def get_context_data(self, ** kwargs):
		context = super(PublisherDetailView, self).get_context_data( ** kwargs)
		return context

class PublisherPublicationsView(SingleObjectMixin, ListView):
	paginate_by = settings.PAGINATE_BY
	template_name = 'manager/publisher/publications.html'
	fields_search = publication.FIELDS_SEARCH

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Publisher.objects.all())
		return super(PublisherPublicationsView, self).get(request, * args, ** kwargs)
	def get_context_data(self, ** kwargs):
		context = super(PublisherPublicationsView, self).get_context_data( ** kwargs)
		context['publisher'] = self.object
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("manager:publisher_publications", kwargs={"slug":self.object.slug, "page":1})
		return context

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Publication.objects.filter(publisher=self.object.id, ** kwargs)
		return Publication.objects.filter(publisher=self.object.id)