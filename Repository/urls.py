from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

import settings

urlpatterns = [
    url(r'^manager/', include('manager.urls', namespace="manager", app_name="manager"), name='manager'),
    url(r'^authentication/', include('authentication.urls', namespace="authentication", app_name="authentication"), name='authentication'),
    url(r'^submission/', include('submission.urls', namespace="submission", app_name="submission"), name='submission'),

    url(r'^about/$', TemplateView.as_view(template_name="Repository/about.html"), name="about"),
    url(r'^terms/$', TemplateView.as_view(template_name="Repository/terms.html"), name="terms"),
    url(r'^policies/$', TemplateView.as_view(template_name="Repository/policies.html"), name="policies"),
    url(r'^contact_us/$', TemplateView.as_view(template_name="Repository/contact_us.html"), name="contact_us"),
	
    
    url(r'^django/', include(admin.site.urls), name='admin'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^rosetta/', include('rosetta.urls')),
]
