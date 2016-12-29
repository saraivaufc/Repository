from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
	url(r'^index/$', RedirectView.as_view(url=reverse_lazy("submission:event_list", kwargs={"page":1})), name="home"),
	url(r'^event/', include('submission.urls.event')),
	url(r'^event/(?P<event_slug>[-\w]+)/submission/', include('submission.urls.submissions')),
	#url(r'^event/(?P<event_slug>[-\w]+)/submission/(?P<submission_slug>[-\w]+)/', include('submission.urls.review')),
]
