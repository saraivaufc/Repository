from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group

from authentication.models import User

class ParticipantListView(ListView):
	template_name = 'authentication/participant/list.html'
	paginate_by = settings.PAGINATE_BY
	fields_search = User.FIELDS_SEARCH

	def get_queryset(self):
		query = self.request.GET.get('query')
		text = self.request.GET.get('text')
		if query and query in dict(self.fields_search):
			kwargs = {("%s__contains" % (query,)):text}
			return User.objects.filter(is_staff=False, is_reviser=False, ** kwargs)
		return User.objects.filter(is_staff=False, is_reviser=False)

	def get_context_data(self, ** kwargs):
		context = super(ParticipantListView, self).get_context_data( ** kwargs)
		context["fields_search"] = self.fields_search
		context["url_search"] = reverse_lazy("authentication:participant_list", kwargs={"page":1})
		return context