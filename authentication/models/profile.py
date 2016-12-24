from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(User):
	is_author = models.BooleanField(verbose_name=_(u"Is Author"), default=False)
	is_advisor = models.BooleanField(verbose_name=_(u"Is Advisor"), default=False)

	def save(self, group=None, *args, **kwargs):
		user = super(Profile, self).save()
		self.set_password(self.password)
		if not group:
			group = "default"
		group = Group.objects.get(name=group)
		self.groups.add(group)

	class Meta:
		verbose_name = _(u'Profile')
		verbose_name_plural = _(u'Profile')