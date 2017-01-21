from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.conf import settings
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from base.views import  SearchResponseMixin, CSVResponseMixin, HierarchyResponseMixin

from authentication.models import User

from manager.models import Publication

from submission.models import Submission, Event
from submission.forms import SubmissionForm

from inbox.views import MessageSendView
	
#***** BASIC FUNCTIONS ******

class SubmissionListView(HierarchyResponseMixin, CSVResponseMixin, ListView):
	template_name = 'submission/submission/list.html'
	paginate_by = settings.PAGINATE_BY
	model = Submission

	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_queryset(self):
		queryset = super(SubmissionListView, self).get_queryset()
		return queryset.filter(user=self.request.user)

class SubmissionDetailView(HierarchyResponseMixin, DetailView):
	template_name = 'submission/submission/detail.html'
	model = Submission
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == self.request.user:
			raise PermissionDenied
		return super(SubmissionDetailView, self).get(request)

class SubmissionCreateView(HierarchyResponseMixin, CreateView):
	template_name = 'submission/submission/form.html'
	model = Submission
	form_class = SubmissionForm
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_event(self):
		return Event.objects.filter(slug=self.kwargs['event_slug']).first()
	
	def get_form(self, * args, ** kwargs):
		return self.form_class(self.get_event(), * args, ** kwargs)

	def get_success_url(self):
		return reverse_lazy('submission:submission_detail', kwargs={'event_slug': self.get_event().slug, 'slug': self.object.slug})

	def get(self, request, * args, ** kwargs):
		if not self.get_event().stage()['type'] == 'submission_open_1':
			raise PermissionDenied
		return super(SubmissionCreateView, self).get(request)

	def post(self, request, * args, ** kwargs):		
		if not self.get_event().stage()['type'] == 'submission_open_1':
			raise PermissionDenied

		form = self.get_form(request.POST, request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		event = self.get_event()
		submission = form.save(commit=False)
		submission.event = event
		submission.user = self.request.user
		submission.address = event.address
		submission.year = event.date.year
		submission.issue_date = datetime.today()
		submission.save()
		return super(SubmissionCreateView, self).form_valid(form)

class SubmissionUpdateView(HierarchyResponseMixin, UpdateView):
	template_name = 'submission/submission/form.html'
	model = Submission
	form_class = SubmissionForm
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_event(self):
		return Event.objects.filter(slug=self.kwargs['event_slug']).first()
	
	def get_form(self, * args, ** kwargs):
		kwargs['instance'] = self.get_object()
		return self.form_class(self.get_event(), * args, ** kwargs)

	def get_success_url(self):
		return reverse_lazy('submission:submission_detail', kwargs={'event_slug': self.get_event().slug, 'slug': self.object.slug})

	def get(self, request, * args, ** kwargs):
		if not self.get_event().stage()['type'] == 'submission_open_1':
			raise PermissionDenied
		return super(SubmissionUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):		
		if not self.get_event().stage()['type'] == 'submission_open_1':
			raise PermissionDenied

		form = self.get_form(request.POST, request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)


class SubmissionDeleteView(HierarchyResponseMixin, DeleteView):
	template_name = 'submission/submission/check_delete.html'
	model = Submission
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_event(self):
		return Event.objects.filter(slug=self.kwargs['event_slug']).first()
	
	def get_success_url(self):
		return reverse_lazy('submission:submission_list', kwargs={'event_slug':self.get_event().slug})

	def get(self, request, * args, ** kwargs):
		if not self.get_event().stage()['type'] == 'submission_open_1' or not self.get_object().user == self.request.user:
			raise PermissionDenied
		return super(SubmissionDeleteView, self).get(request)
	def post(self, request, * args, ** kwargs):
		if not self.get_event().stage()['type'] == 'submission_open_1' or not self.get_object().user == self.request.user:
			raise PermissionDenied
		return super(SubmissionDeleteView, self).post(request)

#***** END BASIC FUNCTIONS ******

class SubmissionsToReviewListView(HierarchyResponseMixin, CSVResponseMixin, ListView):
	template_name = 'submission/submission/to_review/list.html'
	paginate_by = settings.PAGINATE_BY
	model=Submission
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_queryset(self):
		queryset = super(SubmissionsToReviewListView, self).get_queryset()
		if self.request.user.is_reviser:
			return queryset.filter(reviser=self.request.user)
		return queryset

class SubmissionToReviewDetailView(HierarchyResponseMixin, DetailView):
	template_name = 'submission/submission/to_review/detail.html'
	model = Submission
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

class SubmissionChangeReviser(HierarchyResponseMixin, UpdateView):
	template_name = 'submission/submission/change_reviser.html'
	model = Submission
	fields = ['reviser',]
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_event(self):
		return Event.objects.filter(slug=self.kwargs['event_slug']).first()
	
	def get_success_url(self):
		return reverse_lazy('submission:submission_list_to_review', kwargs={'event_slug':self.get_event().slug})

	def form_valid(self, form):
		submission = form.save()
		MessageSendView.send_message(
			from_email=self.request.user.email, 
			to_email=submission.reviser.email,
			subject=_("Review"),
			message=_("You is reviser of: <a href='%(link)s' target='_blank'>%(title)s</a>" % {
				'link': reverse_lazy('submission:submission_detail_to_review', kwargs={'event_slug': self.get_event().slug, 'slug': submission.slug}),
				'title': submission.title, }
			)
		)
		return super(SubmissionChangeReviser, self).form_valid(form)

class SubmissionSubmitFinal(UpdateView):
	model = Submission

	def get_event(self):
		return Event.objects.filter(slug=self.kwargs['event_slug']).first()

	def get_success_url(self):
		return reverse_lazy('submission:submission_list_to_review', kwargs={'event_slug':self.get_event().slug})

	def get(self, request, * args, ** kwargs):
		submission = self.get_object()
		submission.is_final = not submission.is_final
		submission.save()
		if submission.is_final:
			MessageSendView.send_message(
				from_email=request.user.email, 
				to_email=submission.user.email,
				subject=_("Submission publish!"),
				message=_("You publication disponible here: %(link)s" % {'link': submission.get_absolute_url()})
			)
		return HttpResponseRedirect(self.get_success_url())

class SubmissionFinalListView(HierarchyResponseMixin, SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'submission/submission/list_final.html'
	paginate_by = settings.PAGINATE_BY
	model=Submission
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]

	def get_queryset(self):
		queryset = super(SubmissionFinalListView, self).get_queryset()
		return filter(lambda x: x.is_final , queryset)