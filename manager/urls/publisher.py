from django.conf.urls import include, url
from manager.views import PublisherListView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView, PublisherDetailView, PublisherPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), PublisherListView.as_view(), name="publisher_list"),
	url(_(r'^add$'), permission_required('manager.add_publisher')(PublisherCreateView.as_view()), name="publisher_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), PublisherDetailView.as_view(), name="publisher_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_publisher')(PublisherUpdateView.as_view()), name="publisher_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_publisher')(PublisherDeleteView.as_view()), name="publisher_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), PublisherPublicationsView.as_view(), name="publisher_publications"),
]