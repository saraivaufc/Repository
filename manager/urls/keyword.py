from django.conf.urls import include, url
from manager.views import KeywordListView, KeywordCreateView, KeywordUpdateView, KeywordDeleteView, KeywordDetailView, KeywordPublicationsView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), KeywordListView.as_view(), name="keyword_list"),
	url(_(r'^add$'), permission_required('manager.add_keyword')(KeywordCreateView.as_view()), name="keyword_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), KeywordDetailView.as_view(), name="keyword_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('manager.change_keyword')(KeywordUpdateView.as_view()), name="keyword_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('manager.delete_keyword')(KeywordDeleteView.as_view()), name="keyword_delete"),
	url(_(r'^(?P<slug>[-\w]+)/publications$'), KeywordPublicationsView.as_view(), name="keyword_publications"),
]