from django.conf.urls import include, url
from django.contrib import admin

import settings

urlpatterns = [
    url(r'^manager/', include('manager.urls', namespace="manager", app_name="manager"), name='manager'),
    url(r'^authentication/', include('authentication.urls', namespace="authentication", app_name="authentication"), name='authentication'),
    url(r'^submission/', include('submission.urls', namespace="submission", app_name="submission"), name='submission'),
    
    url(r'^django/', include(admin.site.urls), name='admin'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^rosetta/', include('rosetta.urls')),
]
