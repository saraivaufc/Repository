from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group

from base.views import SearchResponseMixin, CSVResponseMixin
from authentication.models import User

class ParticipantListView(SearchResponseMixin, CSVResponseMixin, ListView):
	template_name = 'authentication/participant/list.html'
	paginate_by = settings.PAGINATE_BY
	model = User