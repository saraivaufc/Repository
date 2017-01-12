from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

class Reply(models.Model):
	chat = models.ForeignKey('Chat', verbose_name=_("Chat"), related_name="User", null=False, blank=False)
	chat_manager = models.ForeignKey('ChatManager', verbose_name=_("User"), related_name="inbox_message_send")
	read = models.BooleanField(verbose_name=_("Read"), blank=True, default=False)
	text = models.CharField(verbose_name=_("Text"), max_length=140, null=True, blank=True)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/chat/files/%Y/%m/%d', null=True, blank=True)
	last_modified = models.DateTimeField(verbose_name=_('Last modification'), auto_now=False, default=timezone.now)

	def __unicode__(self):
		return self.text if self.text else _("File")

	class Meta:
		ordering = ['last_modified']
		verbose_name = _(u"Reply")
		verbose_name_plural = _(u"Replies")