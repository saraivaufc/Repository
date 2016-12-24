from django.conf.urls import include, url
from manager.views import KeywordListView, KeywordCreateView, KeywordUpdateView, KeywordDeleteView, KeywordDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', KeywordListView.as_view(), name="admin_keyword_list"),
	url(r'^add/$', permission_required('manager.add_keyword')(KeywordCreateView.as_view()), name="admin_keyword_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', KeywordDetailView.as_view(), name="admin_keyword_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_keyword')(KeywordUpdateView.as_view()), name="admin_keyword_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_keyword')(KeywordDeleteView.as_view()), name="admin_keyword_delete"),
]