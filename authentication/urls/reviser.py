from django.conf.urls import include, url
from authentication.views import ReviserListView, ReviserCreateView, ReviserDeleteView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), permission_required('authentication.list_reviser')(ReviserListView.as_view()), name="reviser_list"),
	url(_(r'^add$'), permission_required('authentication.add_reviser')(ReviserCreateView.as_view()), name="reviser_create"),
	url(_(r'^(?P<pk>[0-9]+)/remove$'), permission_required('authentication.delete_reviser')(ReviserDeleteView.as_view()), name="reviser_delete"),
]