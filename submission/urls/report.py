from django.conf.urls import include, url
from submission.views import ReportSubmissionView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^(?P<event_slug>[-\w]+)/submissions$', permission_required('submission.list_submission_to_review')(ReportSubmissionView.as_view()), name="report_submissions"),
]