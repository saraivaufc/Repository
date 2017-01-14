from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save

class MessageManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="message_manager_user", null=False, blank=False)
	messages_unread = models.IntegerField(verbose_name=_("Messages UnRead"), null=True, blank=True, default=0)

	def __unicode__(self):
		return unicode(self.user)

	class Meta:
		ordering = ['-messages_unread']
		verbose_name = _(u"MessageManager")
		verbose_name_plural = _(u"MessagesManager")


def create_message_manager(sender, instance, created, **kwargs):
	if created:
		MessageManager.objects.get_or_create(user=instance)

post_save.connect(create_message_manager, sender=settings.AUTH_USER_MODEL)
