from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from submission.feed import EventsLatests

urlpatterns = [
	url(_(r'^$'), RedirectView.as_view(url=reverse_lazy('submission:home'), permanent=False)),
	url(_(r'^index$'), TemplateView.as_view(template_name="submission/index.html"), name="home"),
	url(_(r'^event/'), include('submission.urls.event')),
	url(_(r'^event/(?P<event_slug>[-\w]+)/submission/'), include('submission.urls.submissions')),
	url(_(r'^event/(?P<event_slug>[-\w]+)/submission/(?P<submission_slug>[-\w]+)/'), include('submission.urls.review')),
	url(_(r'^report/'), include('submission.urls.report')),
	url(_(r'^feed/$'), EventsLatests(), name="feed"),
]
