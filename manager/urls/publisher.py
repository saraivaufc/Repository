from django.conf.urls import include, url
from manager.views import PublisherListView, PublisherCreateView, PublisherUpdateView, PublisherDeleteView, PublisherDetailView, PublisherPublicationsView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', PublisherListView.as_view(), name="publisher_list"),
	url(r'^add/$', permission_required('manager.add_publisher')(PublisherCreateView.as_view()), name="publisher_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', PublisherDetailView.as_view(), name="publisher_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_publisher')(PublisherUpdateView.as_view()), name="publisher_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_publisher')(PublisherDeleteView.as_view()), name="publisher_delete"),
	url(r'^(?P<slug>[-\w]+)/publications/page=(?P<page>[0-9]+)$', PublisherPublicationsView.as_view(), name="publisher_publications"),
]