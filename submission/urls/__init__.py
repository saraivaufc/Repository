from django.conf.urls import include, url
from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'^index/$', TemplateView.as_view(template_name="submission/index.html"), name="home"),
	url(r'^event/', include('submission.urls.event')),
	url(r'^event/(?P<event_slug>[-\w]+)/submission/', include('submission.urls.submissions')),
	url(r'^reviser/', include('submission.urls.reviser')),	
]
