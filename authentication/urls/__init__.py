from django.conf.urls import include, url

urlpatterns = [
	url(r'^account/', include('authentication.urls.account')),
]
