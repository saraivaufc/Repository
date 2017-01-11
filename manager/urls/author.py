from django.conf.urls import include, url
from manager.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView, AuthorPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), AuthorListView.as_view(), name="author_list"),
	url(_(r'^add$'), permission_required('manager.add_author')(AuthorCreateView.as_view()), name="author_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), AuthorDetailView.as_view(), name="author_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_author')(AuthorUpdateView.as_view()), name="author_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_author')(AuthorDeleteView.as_view()), name="author_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), AuthorPublicationsView.as_view(), name="author_publications"),
]