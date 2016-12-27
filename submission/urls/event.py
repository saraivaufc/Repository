from django.conf.urls import include, url
from submission.views import EventListView, EventCreateView, EventUpdateView, EventDeleteView, EventDetailView
from django.contrib.auth.decorators import permission_required


urlpatterns = [
	url(r'^list/page=(?P<page>[0-9]+)$', EventListView.as_view(), name="event_list"),
	url(r'^add/$', permission_required('submission.add_event')(EventCreateView.as_view()), name="event_create"),
	url(r'^(?P<slug>[-\w]+)/detail/$', EventDetailView.as_view(), name="event_detail"),
	url(r'^(?P<slug>[-\w]+)/edit/$', permission_required('submission.change_event')(EventUpdateView.as_view()), name="event_update"),
	url(r'^(?P<slug>[-\w]+)/delete/$', permission_required('submission.delete_event')(EventDeleteView.as_view()), name="event_delete"),
]