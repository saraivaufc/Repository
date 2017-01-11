from django.conf.urls import include, url
from manager.views import CommunityListView, CommunityCreateView, CommunityUpdateView, CommunityDeleteView, CommunityDetailView, CommunityPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), CommunityListView.as_view(), name="community_list"),
	url(_(r'^add$'), permission_required('manager.add_community')(CommunityCreateView.as_view()), name="community_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), CommunityDetailView.as_view(), name="community_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_community')(CommunityUpdateView.as_view()), name="community_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_community')(CommunityDeleteView.as_view()), name="community_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), CommunityPublicationsView.as_view(), name="community_publications"),
]