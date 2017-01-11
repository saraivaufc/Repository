from django.conf.urls import include, url
from manager.views import SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView, SubjectDetailView, SubjectPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), SubjectListView.as_view(), name="subject_list"),
	url(_(r'^add$'), permission_required('manager.add_subject')(SubjectCreateView.as_view()), name="subject_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), SubjectDetailView.as_view(), name="subject_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_subject')(SubjectUpdateView.as_view()), name="subject_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_subject')(SubjectDeleteView.as_view()), name="subject_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), SubjectPublicationsView.as_view(), name="subject_publications"),
]