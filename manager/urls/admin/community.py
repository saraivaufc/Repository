from django.conf.urls import include, url
from manager.views import CommunityListView, CommunityCreateView, CommunityUpdateView, CommunityDeleteView, CommunityDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', CommunityListView.as_view(), name="admin_community_list"),
	url(r'^add/$', permission_required('manager.add_community')(CommunityCreateView.as_view()), name="admin_community_create"),
	url(r'^(?P<slug>[-\w]+)/detail/page=(?P<page>[0-9]+)$', CommunityDetailView.as_view(), name="admin_community_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_community')(CommunityUpdateView.as_view()), name="admin_community_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_community')(CommunityDeleteView.as_view()), name="admin_community_delete"),
]