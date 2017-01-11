from django.conf.urls import include, url
from authentication.views import ParticipantListView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
	url(r'^list$', permission_required('authentication.list_participant')(ParticipantListView.as_view()), name="participant_list"),
]