from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from inbox.views import ChatListView, ChatCreateView, ChatDetailView

urlpatterns = [
	url(_(r'^list$'), login_required(ChatListView.as_view()), name="chat_list"),
	url(_(r'^add$'), login_required(ChatCreateView.as_view()), name="chat_create"),
	url(_(r'^(?P<slug>[-\w]+)/detail$'), login_required(ChatDetailView.as_view()), name="chat_detail"),
]