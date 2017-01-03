from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from manager.models import Publication

class PublicationsLatests(Feed):
	title = _('RIUFC')
	link = '/manager/'
	description = _("The RIUFC is reported here!")

	def items(self):
		return Publication.objects.filter(is_final=True).order_by('-registration_date')[:10]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.abstract

	def item_link(self, item):
		return reverse_lazy('manager:publication_detail', kwargs={'slug':item.slug})