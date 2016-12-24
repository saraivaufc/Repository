from django.conf.urls import include, url
from django.contrib import admin

import settings

urlpatterns = [
    url(r'^', include('manager.urls', namespace="manager", app_name="manager"), name='manager'),
    url(r'^', include('authentication.urls', namespace="authentication", app_name="authentication"), name='authentication'),
    url(r'^django/', include(admin.site.urls), name='admin'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^rosetta/', include('rosetta.urls')),
]
