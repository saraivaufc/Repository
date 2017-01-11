from django.conf.urls import include, url
from manager.views import CollectionListView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView, CollectionDetailView, CollectionPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), CollectionListView.as_view(), name="collection_list"),
	url(_(r'^add$'), permission_required('manager.add_collection')(CollectionCreateView.as_view()), name="collection_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), CollectionDetailView.as_view(), name="collection_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_collection')(CollectionUpdateView.as_view()), name="collection_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_collection')(CollectionDeleteView.as_view()), name="collection_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), CollectionPublicationsView.as_view(), name="collection_publications"),
]