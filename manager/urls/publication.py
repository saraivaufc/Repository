from django.conf.urls import include, url
from manager.views import PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDeleteView, PublicationDetailView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), PublicationListView.as_view(), name="publication_list"),
	url(_(r'^add$'), permission_required('manager.add_publication')(PublicationCreateView.as_view()), name="publication_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), PublicationDetailView.as_view(), name="publication_detail"),
	url(_(r'^(?P<pk>[0-9]+)$'), PublicationDetailView.as_view(), name="publication_uri"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_publication')(PublicationUpdateView.as_view()), name="publication_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_publication')(PublicationDeleteView.as_view()), name="publication_delete"),
]