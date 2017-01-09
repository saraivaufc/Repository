from django.conf.urls import patterns, url
from manager.api.views import AuthorAPIView


urlpatterns = patterns(
	'manager.api.views',
	url(r'^author$', AuthorAPIView.as_view(), name='api_author'),
	url(r'^author/(?P<pk>[0-9]+)$', AuthorAPIView.as_view(), name='api_author'),
)