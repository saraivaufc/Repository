from django.conf.urls import include, url

urlpatterns = [
	url(r'^account/', include('authentication.urls.account')),
	url(r'^reviser/', include('authentication.urls.reviser')),	
	url(r'^administrator/', include('authentication.urls.administrator')),	
]
