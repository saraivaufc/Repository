from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from manager.feed import PublicationsLatests

urlpatterns = [
	url(_(r'^$'), RedirectView.as_view(url=reverse_lazy('manager:home'), permanent=False)),
	url(_(r'^index$'), TemplateView.as_view(template_name="manager/index.html"), name="home"),
	url(_(r'^community/'), include('manager.urls.community')),
	url(_(r'^collection/'), include('manager.urls.collection')),
	url(_(r'^publisher/'), include('manager.urls.publisher')),
	url(_(r'^subject/'), include('manager.urls.subject')),
	url(_(r'^keyword/'), include('manager.urls.keyword')),
	url(_(r'^author/'), include('manager.urls.author')),
	url(_(r'^publication/'), include('manager.urls.publication')),
	url(_(r'^feed/$'), PublicationsLatests(), name="feed"),
]