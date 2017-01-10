from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from django.http import JsonResponse

from manager.models import Publication
from submission.models import Event, Submission

from base.utils import Export

class ReportSubmissionView(View):
	def get(self, request, * args, ** kwargs):
		export = Export()
		event = Event.objects.filter(slug=self.kwargs['event_slug']).first()
		submissions = Submission.objects.filter(event=event)
		publications = []
		
		for submission in submissions:
			if self.request.POST['type_report'] == 'all':
				pass
			elif self.request.POST['type_report'] == 'with_review' and not submission.review:
				continue
			elif self.request.POST['type_report'] == 'without_review' and submission.review:
				continue
			elif self.request.POST['type_report'] == 'is_final' and not submission.publication.is_final:
				continue
			elif self.request.POST['type_report'] == 'is_not_final' and submission.publication.is_final:
				continue
			publications.append(submission.publication)

		return export.to_csv(request, publications, ('title', 'authors','typology'))