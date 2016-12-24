from django.conf.urls import include, url

urlpatterns = [
	url(r'^index/', include('manager.urls.public.index')),
]
