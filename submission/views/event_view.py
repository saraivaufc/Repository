from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from submission.models import Event

class EventListView(ListView):
	template_name = 'submission/event/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = Event.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return Event.objects.filter(** kwargs)
		return Event.objects.all()

	def get_context_data(self, ** kwargs):
		context = super(EventListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("submission:event_list", kwargs={"page":1})
		return context

class EventCreateView(CreateView):
	template_name = 'submission/event/form.html'
	model = Event
	fields = ['name', 'description', 'address', 'year', 'image', 'typology', 'community', 'publisher', 'date', 
	'submission_1_open', 'submission_1_close', 'review_open', 'review_close', 'submission_2_open', 'submission_2_close']

	def get_success_url(self):
		return reverse_lazy('submission:event_detail', kwargs={'slug':self.object.slug})

	def form_valid(self, form):
		return super(EventCreateView, self).form_valid(form)

class EventUpdateView(UpdateView):
	template_name = 'submission/event/form.html'
	model = Event
	fields = ['name', 'description', 'address','year', 'image', 'typology', 'community', 'publisher', 'date', 
	'submission_1_open', 'submission_1_close', 'review_open', 'review_close', 'submission_2_open', 'submission_2_close']
	
	def get_success_url(self):
		return reverse_lazy('submission:event_detail', kwargs={'slug':self.object.slug})
		
	def form_valid(self, form):
		return super(EventUpdateView, self).form_valid(form)

class EventDeleteView(DeleteView):
	template_name = 'submission/event/check_delete.html'
	model = Event
	success_url = reverse_lazy('submission:event_list', kwargs={'page': 1})

class EventDetailView(DetailView):
	template_name = 'submission/event/detail.html'
	model = Event

	def get_context_data(self, ** kwargs):
		context = super(EventDetailView, self).get_context_data( ** kwargs)
		return context