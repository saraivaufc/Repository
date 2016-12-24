from django.conf.urls import include, url
from manager.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', AuthorListView.as_view(), name="author_list"),
	url(r'^add/$', permission_required('manager.add_author')(AuthorCreateView.as_view()), name="author_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', AuthorDetailView.as_view(), name="author_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_author')(AuthorUpdateView.as_view()), name="author_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_author')(AuthorDeleteView.as_view()), name="author_delete"),
]