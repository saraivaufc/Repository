from django.conf.urls import include, url
from submission.views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView, ReviewDetailView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^add$'), permission_required('submission.add_review')(ReviewCreateView.as_view()), name="review_create"),
	url(_(r'^(?P<pk>[-\w]+)/detail$'), ReviewDetailView.as_view(template_name="submission/review/detail.html"), name="review_detail"),
	url(_(r'^(?P<pk>[-\w]+)/detail_to_review$'), ReviewDetailView.as_view(template_name="submission/review/detail_to_review.html"), name="review_detail_to_review"),
	url(_(r'^(?P<pk>[-\w]+)/edit$'), permission_required('submission.change_review')(ReviewUpdateView.as_view()), name="review_update"),
	url(_(r'^(?P<pk>[-\w]+)/delete$'), permission_required('submission.delete_review')(ReviewDeleteView.as_view()), name="review_delete"),
]