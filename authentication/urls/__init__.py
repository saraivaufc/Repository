from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^account/'), include('authentication.urls.account')),
	url(_(r'^participant/'), include('authentication.urls.participant')),
	url(_(r'^reviser/'), include('authentication.urls.reviser')),	
	url(_(r'^administrator/'), include('authentication.urls.administrator')),	
]
