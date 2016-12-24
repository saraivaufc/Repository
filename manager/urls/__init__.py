from django.conf.urls import include, url
from manager.views import home

urlpatterns = [
	url(r'^index/$', TemplateView.as_view(template_name="manager/index.html"), name="home"),
	url(r'^community/', include('manager.urls.community')),
	url(r'^collection/', include('manager.urls.collection')),
	url(r'^publisher/', include('manager.urls.publisher')),
	url(r'^subject/', include('manager.urls.subject')),
	url(r'^keyword/', include('manager.urls.keyword')),
	url(r'^author/', include('manager.urls.author')),
	url(r'^publication/', include('manager.urls.publication')),
]
