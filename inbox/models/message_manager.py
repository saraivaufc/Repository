from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save

class MessageManager(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="message_manager_user", null=False, blank=False)
	
	def get_messages_receive(self):
		from inbox.models import Message
		messages = Message.objects.filter(message_manager_receive=self).exclude(message_manager_send=self)
		return messages

	def get_messages_send(self):
		from inbox.models import Message
		messages = Message.objects.filter(message_manager_send=self).exclude(message_manager_receive=self)
		return messages

	def get_drafts(self):
		from inbox.models import Message
		drafts = Message.objects.filter(message_manager_send=self, message_manager_receive=self)
		return drafts

	def get_messages_unread(self):
		return self.get_messages_receive().filter(read=False)

	def __unicode__(self):
		return unicode(self.user)

	class Meta:
		ordering = ['user']
		verbose_name = _(u"Message Manager")
		verbose_name_plural = _(u"Messages Manager")


def create_message_manager(sender, instance, created, **kwargs):
	if created:
		MessageManager.objects.get_or_create(user=instance)

post_save.connect(create_message_manager, sender=settings.AUTH_USER_MODEL)
