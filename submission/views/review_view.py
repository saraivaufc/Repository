from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from datetime import datetime
from django.http import HttpResponseRedirect

from authentication.models import User
from submission.models import Review, Submission, Event

class ReviewCreateView(CreateView):
	template_name = 'submission/review/form.html'
	model = Review
	fields = ['originality', 'originality_observation', 'technical_merit', 'technical_merit_observation', 
	'clarity', 'clarity_observation','text_quality', 'text_quality_observation', 'relevance', 
	'relevance_observation', 'knowledge_level_revisor', 'knowledge_level_revisor_observation', 'general', 'general_observation',]

	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		return reverse_lazy('submission:review_detail_to_review', kwargs={'event_slug':event.slug, 'submission_slug':submission.slug, 'pk': self.object.pk,})

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		if not request.user == submission.reviser:
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug, 'page': 1}))
		return super(ReviewCreateView, self).get(request)	

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()

		context = super(ReviewCreateView, self).get_context_data( ** kwargs)
		context["event"] = event
		context["submission"] = submission
		context["publication"] = submission.publication
		context["review"] = self.object
		return context

	def form_valid(self, form):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()

		review = form.save()
		submission.review = review
		submission.save()
		return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(UpdateView):
	template_name = 'submission/review/form.html'
	model = Review
	fields = ['originality', 'originality_observation', 'technical_merit', 'technical_merit_observation', 
	'clarity', 'clarity_observation','text_quality', 'text_quality_observation', 'relevance', 
	'relevance_observation', 'knowledge_level_revisor', 'knowledge_level_revisor_observation', 'general', 'general_observation',]

	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		return reverse_lazy('submission:review_detail_to_review', kwargs={'event_slug':event.slug, 'submission_slug':submission.slug, 'pk': self.object.pk,})

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		if not request.user == submission.reviser:
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug, 'page': 1}))
		return super(ReviewUpdateView, self).get(request)

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()

		context = super(ReviewUpdateView, self).get_context_data( ** kwargs)
		context["event"] = event
		context["submission"] = submission
		context["publication"] = submission.publication
		context["review"] = self.object
		return context

class ReviewDeleteView(DeleteView):
	template_name = 'submission/review/check_delete.html'
	model = Review

	def get_success_url(self):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		return reverse_lazy('submission:submission_detail_to_review', kwargs={'event_slug':event.slug, 'slug':submission.slug,})

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()

		context = super(ReviewDeleteView, self).get_context_data( ** kwargs)
		context["event"] = event
		context["submission"] = submission
		context["publication"] = submission.publication
		context["review"] = self.object
		return context

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		if not request.user == submission.reviser:
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug, 'page': 1}))
		return super(ReviewDeleteView, self).get(request)
	def post(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		submission.review = None
		submission.save()
		return super(ReviewDeleteView, self).post(request)

class ReviewDetailView(DetailView):
	model = Review

	def get_context_data(self, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()
		context = super(ReviewDetailView, self).get_context_data( ** kwargs)
		context['event'] = event
		context['publication'] = submission.publication
		context['submission'] = submission
		context['review'] = self.object
		return context

	def get(self, request, * args, ** kwargs):
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submission = Submission.objects.filter(slug=self.kwargs['submission_slug']).first()

		if request.user == submission.user or request.user == submission.reviser or request.user.is_staff:
			return super(ReviewDetailView, self).get(request)
		else:
			return HttpResponseRedirect(reverse_lazy('submission:submission_list', kwargs={'event_slug':event.slug, 'page': 1}))