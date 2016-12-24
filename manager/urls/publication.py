from django.conf.urls import include, url
from manager.views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView, PublicationDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', PublicationListView.as_view(), name="publication_list"),
	url(r'^add/$', permission_required('manager.add_publication')(PublicationCreateView.as_view()), name="publication_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', PublicationDetailView.as_view(), name="publication_detail"),
	url(r'^(?P<pk>[0-9]+)/$', PublicationDetailView.as_view(), name="publication_uri"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_publication')(PublicationUpdateView.as_view()), name="publication_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_publication')(PublicationDeleteView.as_view()), name="publication_delete"),
]