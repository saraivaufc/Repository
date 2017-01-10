from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools
import datetime

from manager.models import Community, Collection, Publisher

class Event(models.Model):
	TYPOLOGY_CHOICES = (
		(u'conference', _(u'Conference')),
		(u'workshop', _(u'Workshop')),
	)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=500, blank=True, unique=True)
	name = models.CharField(verbose_name=_("Name"), max_length=100, null=False, blank=False)
	description = models.TextField(verbose_name=_("description"), null=False, blank=False)
	address = models.CharField(verbose_name=_("Address"), max_length=100, null=False, blank=False)
	year = models.IntegerField(verbose_name=_("Year"), null=False, blank=False)
	image = models.FileField(verbose_name=_(u"Image"), upload_to='documents/event/images/%Y/%m/%d')
	typology = models.CharField(verbose_name=_("Typology"), choices=TYPOLOGY_CHOICES, max_length=100, null=False, blank=False)
	community = models.ForeignKey(Community, verbose_name=_("Community"), null=False, blank=False)
	publisher = models.ForeignKey(Publisher, verbose_name=_("Publisher"), null=False, blank=False)
	date = models.DateField(verbose_name=_("Date"), null=False, blank=False)
	
	submission_1_open = models.DateField(verbose_name=_("Submission 1 Open"), null=False, blank=False)
	submission_1_close = models.DateField(verbose_name=_("Submission 1 Close"), null=False, blank=False)

	review_open = models.DateField(verbose_name=_("Review Open"), null=False, blank=False)
	review_close = models.DateField(verbose_name=_("Review Close"), null=False, blank=False)
	
	submission_2_open = models.DateField(verbose_name=_("Submission 2 Open"), null=False, blank=False)
	submission_2_close = models.DateField(verbose_name=_("Submission 2 Close"), null=False, blank=False)

	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def get_search_fields():
		return (
			("name", _("Name")),
			("description", _("Description")),
		)
	def get_output_fields():
		return (
			("name", _("Name")),
			("typology", _("Typology")),
			("address", _("Address")),
			("community", _("Community")),
			("publisher", _("Publisher")),
			("date", _("Date")),
			("submission_1_open", _("Submission 1 Open")),
			("review_open", _("Review Open")),
			("submission_2_open", _("Submission 2 Open")),
				
		)

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def stage(self):
		now = datetime.date.today()
		if now < self.submission_1_open:
			return {'type': 'before_period', 'text': _('Before the period')}
		elif self.submission_1_open <= now <= self.submission_1_close:
			return {'type': 'submission_open_1', 'text': _('Submission Open 1')}
		elif self.submission_1_close < now < self.submission_2_open:
			return {'type': 'reviewing', 'text': _('Reviewing...')}
		elif self.submission_2_open <= now <= self.submission_2_close:
			return {'type': 'submission_open_2', 'text': _('Submission Open 2')}
		elif now > self.submission_2_close:
			return {'type': 'submission_complete', 'text': _('Submission Complete')}
		else:
			return {'type': 'out_of_period', 'text': _('Out of period')}

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Event.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Event, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def natural_key(self):
		return self.name

	def verbose_name(self):
		return self._meta.verbose_name

	class Meta:
		ordering = ['-date']
		verbose_name = _(u'Event')
		verbose_name_plural = _(u'Event')