from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from django.template.defaultfilters import slugify

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
	first_name = models.CharField(verbose_name=_(u"First Name "), max_length=100, blank=True, null=True, help_text=_(u'Please enter you first name.'), )
	last_name = models.CharField(verbose_name=_(u"Last Name "), max_length=100, blank=True, null=True, help_text=_(u'Please enter you last name.'), )
	username = models.CharField(verbose_name=_(u"Username"), max_length=254, unique=True,  null=False, blank=False, help_text=_(u'Please enter you username.'), )
	email = models.EmailField(verbose_name=_(u"Email"), max_length=254, unique=True,  null=False, blank=False, help_text=_(u'Please enter you email.'), )
	is_active = models.BooleanField(verbose_name=_('Active'), default=True, help_text=_(u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(verbose_name=_(u'Date joined'), default=timezone.now)
	is_moderator = models.BooleanField(_('Moderator Status'), default=False, blank=True)
	is_staff = models.BooleanField(_(u'Staff Status'), default=False,)
	is_reviser = models.BooleanField(_(u'Reviser Status'), default=False,)

	REQUIRED_FIELDS =[]
	USERNAME_FIELD = 'email'

	objects = UserManager()

	def get_search_fields():
		return (
			("first_name", _("First Name")), 
			("last_name", _("Last Name")),
			("username", _("Username")),
			("email", _("Email")),
		)
	def get_output_fields():
		return (
			("first_name", _("First Name")), 
			("last_name", _("Last Name")),
			("username", _("Username")),
			("email", _("Email")),
		)

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def get_full_name(self):
		if self.first_name and self.last_name:
			return self.first_name + ' ' + self.last_name
		elif self.first_name:
			return first_name
		elif self.last_name:
			return self.last_name
		else:
			return None

	def get_short_name(self):
		return self.email

	def save(self, group=None, *args, **kwargs):
		if not self.username:
			self.username = self.email
		user = super(User, self).save()
		if group:
			group = Group.objects.get(name=group)
			self.groups.add(group)

	def __unicode__(self):
		return self.email

	def natural_key(self):
		return self.email

	def verbose_name(self):
		return self._meta.verbose_name

	class Meta:
		verbose_name = _(u'User')
		verbose_name_plural = _(u'User')
		permissions = (
			("list_participant", "List Participant"),
			("list_reviser", "List Reviser"),
			("add_reviser", "Add Reviser"),
			("change_reviser", "Change Reviser"),
			("delete_reviser", "Delete Reviser"),
			("list_administrator", "List Administrator"),
			("add_administrator", "Add Administrator"),		
			("delete_administrator", "Delete Administrator"),
		)