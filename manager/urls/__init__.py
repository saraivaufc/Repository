from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from manager.feed import PublicationsLatests

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('manager:home'), permanent=True)),
	url(r'^index/$', TemplateView.as_view(template_name="manager/index.html"), name="home"),
	url(r'^community/', include('manager.urls.community')),
	url(r'^collection/', include('manager.urls.collection')),
	url(r'^publisher/', include('manager.urls.publisher')),
	url(r'^subject/', include('manager.urls.subject')),
	url(r'^keyword/', include('manager.urls.keyword')),
	url(r'^author/', include('manager.urls.author')),
	url(r'^publication/', include('manager.urls.publication')),
	url(r'^feed/$', PublicationsLatests(), name="feed"),
]