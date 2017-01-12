from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
import itertools
from django.db import models
from django.utils import timezone

class Chat(models.Model):
	slug = models.SlugField(verbose_name=_('slug'), max_length=100, blank=True, unique=True)
	chat_manager_send = models.ForeignKey('ChatManager', verbose_name=_("From"), related_name="inbox_manager_request", null=False, blank=False)
	chat_manager_receive = models.ForeignKey('ChatManager', verbose_name=_("To"), related_name="inbox_manager_response", null=False, blank=False)
	subject = models.CharField(verbose_name=_("Subject"), max_length=140)
	text = models.TextField(verbose_name=_("Text"), null=True, blank=True)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/chat/files/%Y/%m/%d', null=True, blank=True)
	message_unread = models.BooleanField(verbose_name=_("Message UnRead"), blank=True, default=False)
	last_modified = models.DateTimeField(verbose_name=_('Last modification'), auto_now=False, default=timezone.now)

	def get_replies(self):
		from inbox.models import Reply
		replies = Reply.objects.filter(chat=self)
		return replies

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.subject)
			for x in itertools.count(1):
				if not Chat.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Chat, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return unicode(self.chat_manager_send) + '->' +  unicode(self.chat_manager_receive)

	class Meta:
		ordering = ['-last_modified']
		verbose_name = _(u"Chat")
		verbose_name_plural = _(u"Chats")