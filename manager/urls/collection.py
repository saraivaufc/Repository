from django.conf.urls import include, url
from manager.views import CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView, CollectionDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', CollectionListView.as_view(), name="collection_list"),
	url(r'^add/$', permission_required('manager.add_collection')(CollectionCreateView.as_view()), name="collection_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', CollectionDetailView.as_view(), name="collection_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_collection')(CollectionUpdateView.as_view()), name="collection_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_collection')(CollectionDeleteView.as_view()), name="collection_delete"),
]