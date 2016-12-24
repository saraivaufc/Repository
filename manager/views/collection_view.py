from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings


from manager.models import Collection

class CollectionListView(ListView):
	template_name = 'manager/collection/list.html'
	paginate_by = settings.PAGINATE_BY
	queryset = Collection.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(CollectionListView, self).get_context_data( ** kwargs)
		return context

class CollectionCreateView(CreateView):
	template_name = 'manager/collection/form.html'
	model = Collection
	fields = ['community','name', 'description']
	success_url = reverse_lazy('manager:collection_list', kwargs={'page': 1})

	def form_valid(self, form):
		return super(CollectionCreateView, self).form_valid(form)

class CollectionUpdateView(UpdateView):
	template_name = 'manager/collection/form.html'
	model = Collection
	fields = ['community','name', 'description']
	success_url = reverse_lazy('manager:collection_list', kwargs={'page': 1})
	
	def form_valid(self, form):
		return super(CollectionUpdateView, self).form_valid(form)

class CollectionDeleteView(DeleteView):
	template_name = 'manager/collection/check_delete.html'
	model = Collection
	success_url = reverse_lazy('manager:collection_list', kwargs={'page': 1})

class CollectionDetailView(DetailView):
	template_name = 'manager/collection/detail.html'
	model = Collection

	def get_context_data(self, ** kwargs):
		context = super(CollectionDetailView, self).get_context_data( ** kwargs)
		return context