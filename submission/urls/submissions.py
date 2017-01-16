from django.conf.urls import include, url
from submission.views import SubmissionListView, SubmissionsToReviewListView, SubmissionCreateView, SubmissionUpdateView, SubmissionDeleteView, SubmissionDetailView, SubmissionChangeReviser, SubmissionToReviewDetailView, SubmissionSubmitFinal, SubmissionFinalListView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), SubmissionListView.as_view(), name="submission_list"),
	url(_(r'^list_all$'), permission_required('submission.list_submission_to_review')(SubmissionsToReviewListView.as_view()), name="submission_list_to_review"),
	url(_(r'^add$'), permission_required('submission.add_submission')(SubmissionCreateView.as_view()), name="submission_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), SubmissionDetailView.as_view(), name="submission_detail"),
	url(_(r'^(?P<slug>[-\w]+)/detail_to_review$'), SubmissionToReviewDetailView.as_view(), name="submission_detail_to_review"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('submission.change_submission')(SubmissionUpdateView.as_view()), name="submission_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('submission.delete_submission')(SubmissionDeleteView.as_view()), name="submission_delete"),
	url(_(r'^(?P<slug>[-\w]+)/add_reviser$'), permission_required('authentication.change_reviser')(SubmissionChangeReviser.as_view()), name="submission_change_reviser"),
	url(_(r'^(?P<slug>[-\w]+)/submit_final$'), permission_required('submission.submit_final')(SubmissionSubmitFinal.as_view()), name="submission_submit_final"),
	url(_(r'^submission_final$'), permission_required('submission.submit_final')(SubmissionFinalListView.as_view()), name="submission_final"),
]