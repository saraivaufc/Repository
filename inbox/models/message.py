from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
import itertools
from django.db import models
from django.utils import timezone

class Message(models.Model):
	slug = models.SlugField(verbose_name=_('slug'), max_length=100, blank=True, unique=True)
	message_manager_send = models.ForeignKey('MessageManager', verbose_name=_("From"), related_name="inbox_manager_request", null=False, blank=False)
	message_manager_receive = models.ForeignKey('MessageManager', verbose_name=_("To"), related_name="inbox_manager_response", null=False, blank=False)
	subject = models.CharField(verbose_name=_("Subject"), max_length=140)
	text = models.TextField(verbose_name=_("Text"), null=True, blank=True)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/message/files/%Y/%m/%d', null=True, blank=True)
	message_read = models.BooleanField(verbose_name=_("Message Read"), blank=True, default=False)
	last_modified = models.DateTimeField(verbose_name=_('Last modification'), auto_now=False, default=timezone.now)

	def get_replies(self):
		from inbox.models import Reply
		replies = Reply.objects.filter(message=self)
		return replies

	def get_type(self, message_manager):
		if message_manager == self.message_manager_send and message_manager != self.message_manager_receive:
			return "sends"
		elif message_manager != self.message_manager_send and message_manager == self.message_manager_receive:
			return "receives"
		elif message_manager == self.message_manager_send and message_manager == self.message_manager_receive:
			return "drafts"
		else:
			return None

	def get_search_fields():
		return (
			("subject", _("Subject")),
			("text", _("Text")),
		)
	def get_types():
		return {
			"receives":_("receives"),
			"sends": _("sends"),
			"drafts": _("drafts"),
		}

	get_search_fields = staticmethod(get_search_fields)
	get_types = staticmethod(get_types)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.subject)
			for x in itertools.count(1):
				if not Message.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Message, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return unicode(self.message_manager_send) + '->' +  unicode(self.message_manager_receive)

	def natural_key(self):
		return self.__unicode__()

	def verbose_name(self):
		return self._meta.verbose_name

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _(u"Message")
		verbose_name_plural = _(u"Messages")