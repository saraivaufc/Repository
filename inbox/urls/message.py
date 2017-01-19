from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from inbox.views import MessageListView, MessageCreateView, MessageDetailView

urlpatterns = [
	url(_(r'^receives/list$'), login_required(MessageListView.as_view(query='receives')), name="message_list_receives"),
	url(_(r'^sends/list$'), login_required(MessageListView.as_view(query='sends')), name="message_list_sends"),
	url(_(r'^drafts/list$'), login_required(MessageListView.as_view(query='drafts')), name="message_list_drafts"),
	url(_(r'^send$'), login_required(MessageCreateView.as_view()), name="message_send"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), login_required(MessageDetailView.as_view()), name="message_detail"),
]