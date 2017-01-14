from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

class Reply(models.Model):
	message = models.ForeignKey('Message', verbose_name=_("Message"), related_name="User", null=False, blank=False)
	message_manager = models.ForeignKey('MessageManager', verbose_name=_("User"), related_name="inbox_message_send")
	read = models.BooleanField(verbose_name=_("Read"), blank=True, default=False)
	text = models.TextField(verbose_name=_("Text"), null=True, blank=True)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/message/files/%Y/%m/%d', null=True, blank=True)
	last_modified = models.DateTimeField(verbose_name=_('Last modification'), auto_now=False, default=timezone.now)

	def __unicode__(self):
		return self.text if self.text else _("File")

	class Meta:
		ordering = ['last_modified']
		verbose_name = _(u"Reply")
		verbose_name_plural = _(u"Replies")