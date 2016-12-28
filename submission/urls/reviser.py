from django.conf.urls import include, url
from submission.views import ReviserListView, ReviserCreateView, ReviserDeleteView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', permission_required('submission.list_reviser')(ReviserListView.as_view()), name="reviser_list"),
	url(r'^add/$', permission_required('submission.add_reviser')(ReviserCreateView.as_view()), name="reviser_create"),
	url(r'^(?P<pk>[0-9]+)/remove/$', permission_required('submission.delete_reviser')(ReviserDeleteView.as_view()), name="reviser_delete"),
]