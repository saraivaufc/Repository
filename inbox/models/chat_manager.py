from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

class ChatManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="chat_manager_user", null=False, blank=False)
	messages_unread = models.IntegerField(verbose_name=_("Messages UnRead"), null=True, blank=True, default=0)

	def __unicode__(self):
		return unicode(self.user)

	class Meta:
		ordering = ['-messages_unread']
		verbose_name = _(u"ChatManager")
		verbose_name_plural = _(u"ChatsManager")