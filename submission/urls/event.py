from django.conf.urls import include, url
from submission.views import EventListView, EventCreateView, EventUpdateView, EventDeleteView, EventDetailView
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^list$'), EventListView.as_view(), name="event_list"),
	url(_(r'^add$'), permission_required('submission.add_event')(EventCreateView.as_view()), name="event_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), EventDetailView.as_view(), name="event_detail"),
	url(_(r'^(?P<slug>[-\w]+)/edit$'), permission_required('submission.change_event')(EventUpdateView.as_view()), name="event_update"),
	url(_(r'^(?P<slug>[-\w]+)/delete$'), permission_required('submission.delete_event')(EventDeleteView.as_view()), name="event_delete"),
]