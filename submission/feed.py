from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from submission.models import Event

class EventsLatests(Feed):
	title = _('RIUFC')
	link = '/submission/'
	description = _("The RIUFC is reported here!")

	def items(self):
		return Event.objects.all().order_by('-registration_date')[:10]

	def item_title(self, item):
		return item.name

	def item_description(self, item):
		return item.description

	def item_link(self, item):
		return reverse_lazy('submission:event_detail', kwargs={'slug':item.slug})