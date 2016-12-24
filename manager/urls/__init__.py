from django.conf.urls import include, url
from manager.views import home

urlpatterns = [
	url(r'^admin/', include('manager.urls.admin')),
	url(r'^public/', include('manager.urls.public')),
	url(r'^$', home, name="home"),
]
