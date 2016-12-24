from django.conf.urls import include, url

urlpatterns = [
	url(r'^community/', include('manager.urls.admin.community')),
	url(r'^collection/', include('manager.urls.admin.collection')),
	url(r'^publisher/', include('manager.urls.admin.publisher')),
	url(r'^subject/', include('manager.urls.admin.subject')),
	url(r'^keyword/', include('manager.urls.admin.keyword')),
	url(r'^author/', include('manager.urls.admin.author')),
	url(r'^publication/', include('manager.urls.admin.publication')),
]