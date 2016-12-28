from django.conf.urls import include, url
from authentication.views import AdministratorListView, AdministratorCreateView, AdministratorDeleteView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', permission_required('authentication.list_administrator')(AdministratorListView.as_view()), name="administrator_list"),
	url(r'^add/$', permission_required('authentication.add_administrator')(AdministratorCreateView.as_view()), name="administrator_create"),
	url(r'^(?P<pk>[0-9]+)/remove/$', permission_required('authentication.delete_administrator')(AdministratorDeleteView.as_view()), name="administrator_delete"),
]