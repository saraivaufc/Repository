from django.conf.urls import include, url
from manager.views import SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView, SubjectDetailView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', SubjectListView.as_view(), name="admin_subject_list"),
	url(r'^add/$', permission_required('manager.add_subject')(SubjectCreateView.as_view()), name="admin_subject_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', SubjectDetailView.as_view(), name="admin_subject_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('manager.change_subject')(SubjectUpdateView.as_view()), name="admin_subject_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('manager.delete_subject')(SubjectDeleteView.as_view()), name="admin_subject_delete"),
]