from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
	def create_user(self, email, password, group='participant'):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(group=group)
		return user
	def create_superuser(self, email, password, group='administrator'):
		user = self.create_user(email,
			password=password,
		)
		user.is_superuser = True
		user.is_moderator = True
		user.is_staff = True
		user.save(group=group)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(verbose_name=_(u"First Name "), max_length=100, blank=False, null=False, help_text=_(u'Please enter you first name.'), )
	last_name = models.CharField(verbose_name=_(u"Last Name "), max_length=100, blank=False, null=False, help_text=_(u'Please enter you last name.'), )
	email = models.EmailField(verbose_name=_(u"Email"), max_length=254, unique=True,  null=False, blank=False, help_text=_(u'Please enter you email.'), )
	is_active = models.BooleanField(verbose_name=_('active'), default=True, help_text=_(u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(verbose_name=_(u'date joined'), default=timezone.now)
	is_moderator = models.BooleanField(_('moderator status'), default=False, blank=True)
	is_staff = models.BooleanField(_(u'staff status'), default=False,)

	REQUIRED_FIELDS =[]
	USERNAME_FIELD = 'email'

	objects = UserManager()

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __str__(self):
		return self.email

	def __unicode__(self):
		return self.email

	def save(self, group=None, *args, **kwargs):
		user = super(User, self).save()
		if group:
			group = Group.objects.get(name=group)
			self.groups.add(group)

	class Meta:
		verbose_name = _(u'User')
		verbose_name_plural = _(u'User')