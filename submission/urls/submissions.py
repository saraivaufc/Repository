from django.conf.urls import include, url
from submission.views import SubmissionListView, SubmissionCreateView, SubmissionUpdateView, SubmissionDeleteView, SubmissionDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', SubmissionListView.as_view(), name="submission_list"),
	url(r'^add/$', permission_required('submission.add_submission')(SubmissionCreateView.as_view()), name="submission_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', SubmissionDetailView.as_view(), name="submission_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('submission.change_submission')(SubmissionUpdateView.as_view()), name="submission_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('submission.delete_submission')(SubmissionDeleteView.as_view()), name="submission_delete"),
]