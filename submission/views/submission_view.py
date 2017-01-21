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

from base.views import  SearchResponseMixin, CSVResponseMixin, HierarchyResponseMixin

from authentication.models import User

from manager.models import Publication

from submission.models import Submission, Event
from submission.forms import SubmissionForm

from inbox.views import MessageSendView
		
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

class SubmissionCreateView(HierarchyResponseMixin, CreateView):
	template_name = 'submission/submission/form.html'
	model = Publication
	form_class = SubmissionForm
	hierarchy_fields= [
		{'name':'event', 'id': 'slug', 'slug':'event_slug', 'model': Event},
	]
	event = None

	def get_event(self):
		if not self.event:
			self.event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		return self.event
	
	def get_form(self):
		form = self.form_class(event=self.get_event())
		return form

	def get_success_url(self):
		return reverse_lazy('submission:submission_list', kwargs={'event_slug':self.get_event().slug})

	def get(self, request, * args, ** kwargs):
		event = self.get_event()
		if not event.stage()['type'] == 'submission_open_1':
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionCreateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		form = self.form_class(self.get_event(), request.POST, request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		publication = form.save(commit=False)
		publication.address = event.address
		publication.year = event.date.year
		publication.issue_date = datetime.today()
		publication.save()
		submission = Submission(event=self.get_event(),
								user=self.request.user, 
								publication=publication,)
		submission.save()
		return super(SubmissionCreateView, self).form_valid(form)

class SubmissionUpdateView(UpdateView):
	template_name = 'submission/submission/form.html'
	model = Publication
	fields = ['title', 'typology', 'subjects', 'authors', 'collection', 'reference','principal_language', 'principal_abstract', 'principal_keywords', 'secondary_language', 'secondary_abstract', 'secondary_keywords', 'file']
	
	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		return reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug})

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context = super(SubmissionUpdateView, self).get_context_data( ** kwargs)	
		context['event'] = event
		context['publication'] = self.object
		return context

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not Submission.objects.filter(event=event, user=self.request.user, publication=self.get_object()):
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionUpdateView, self).get(request)
	def post(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not Submission.objects.filter(event=event, user=self.request.user, publication=self.get_object()):
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionUpdateView, self).post(request)

	def form_valid(self, form):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		publication = form.save(commit=False)
		publication.issue_date = datetime.today()
		publication.save()
		return super(SubmissionUpdateView, self).form_valid(form)

class SubmissionChangeReviser(UpdateView):
	template_name = 'submission/submission/change_reviser.html'
	model = Submission
	fields = ['reviser',]
	
	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		return reverse_lazy('submission:submission_list_to_review', kwargs={'event_slug':event.slug})

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context = super(SubmissionChangeReviser, self).get_context_data( ** kwargs)	
		context['event'] = event
		return context

	def form_valid(self, form):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = form.save()
		MessageSendView.send_message(
			from_email=self.request.user.email, 
			to_email=submission.reviser.email,
			subject=_("Review"),
			message=_("You is reviser of: <a href='%(link)s' target='_blank'>%(title)s</a>" % {
				'link': reverse_lazy('submission:submission_detail_to_review', kwargs={'event_slug': event.slug, 'slug': submission.slug}),
				'title': submission.publication.title, }
			)
		)
		return super(SubmissionChangeReviser, self).form_valid(form)

class SubmissionDeleteView(DeleteView):
	template_name = 'submission/submission/check_delete.html'
	model = Submission

	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		return reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug})

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not Submission.objects.filter(event=event, user=self.request.user,publication=self.get_object().publication):
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionDeleteView, self).get(request)
	def post(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not Submission.objects.filter(event=event, user=self.request.user, publication=self.get_object().publication):
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionDeleteView, self).post(request)

class SubmissionDetailView(DetailView):
	template_name = 'submission/submission/detail.html'
	model = Submission

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context = super(SubmissionDetailView, self).get_context_data( ** kwargs)
		context['event'] = event
		context['publication'] = self.object.publication
		context['submission'] = self.object
		return context

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not Submission.objects.filter(event=event, user=self.request.user,publication=self.get_object().publication):
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug}))
		return super(SubmissionDetailView, self).get(request)


class SubmissionsToReviewListView(CSVResponseMixin, ListView):
	template_name = 'submission/submission/to_review/list.html'
	paginate_by = settings.PAGINATE_BY
	model=Submission

	def get_queryset(self):
		queryset = super(SubmissionsToReviewListView, self).get_queryset()
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if self.request.user.is_reviser:
			return queryset.filter(event=event,reviser=self.request.user)
		else:
			return queryset.filter(event=event)

	def get_context_data(self, ** kwargs):
		context = super(SubmissionsToReviewListView, self).get_context_data( ** kwargs)
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context["event"] = event
		return context

class SubmissionToReviewDetailView(DetailView):
	template_name = 'submission/submission/to_review/detail.html'
	model = Submission

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context = super(SubmissionToReviewDetailView, self).get_context_data( ** kwargs)
		context['event'] = event
		context['publication'] = self.object.publication
		context['submission'] = self.object
		return context

class SubmissionSubmitFinal(UpdateView):
	model = Submission
	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['slug']).first()
		if submission and event:
			submission.publication.is_final = not submission.publication.is_final
			submission.publication.save()
			if submission.publication.is_final:
				MessageSendView.send_message(
					from_email=request.user.email, 
					to_email=submission.user.email,
					subject=_("Submission publish!"),
					message=_("You publication disponible here: %(link)s" % {'link': submission.publication.get_absolute_url()})
				)
		return HttpResponseRedirect(reverse_lazy('submission:submission_list_to_review', kwargs={'event_slug':event.slug}))

class SubmissionFinalListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'submission/submission/list_final.html'
	paginate_by = settings.PAGINATE_BY
	model=Submission

	def get_queryset(self):
		queryset = super(SubmissionFinal, self).get_queryset()
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		return filter(lambda x: x.publication.is_final , queryset.filter(event=event))

	def get_context_data(self, ** kwargs):
		context = super(SubmissionFinal, self).get_context_data( ** kwargs)
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		context["event"] = event
		return context