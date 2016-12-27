from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools
import datetime

from manager.models import Community, Collection, Publisher

FIELDS_SEARCH = (
	("name", _("Name")),
	("description", _("Description")),
)

TYPOLOGY_CHOICES = (
    (u'conference', _(u'Conference')),
    (u'workshop', _(u'Workshop')),
)

class Event(models.Model):
	slug = models.SlugField(verbose_name=_('Slug'), max_length=500, blank=True, unique=True)
	name = models.CharField(verbose_name=_("Name"), max_length=100, null=False, blank=False)
	description = models.TextField(verbose_name=_("Description"), null=False, blank=False)
	address = models.CharField(verbose_name=_("Address"), max_length=100, null=False, blank=False)
	year = models.IntegerField(verbose_name=_("Year"), null=False, blank=False)
	image = models.FileField(verbose_name=_(u"Image"), upload_to='documents/event/images/%Y/%m/%d')
	typology = models.CharField(verbose_name=_("Typology"), choices=TYPOLOGY_CHOICES, max_length=100, null=False, blank=False)
	community = models.ForeignKey(Community, verbose_name=_("Community"), null=False, blank=False)
	collection = models.ForeignKey(Collection, verbose_name=_("Collection"), null=False, blank=False)
	publisher = models.ForeignKey(Publisher, verbose_name=_("Publisher"), null=False, blank=False)
	date = models.DateField(verbose_name=_("Date"), null=False, blank=False)
	
	submission_1_open = models.DateField(verbose_name=_("Submission 1 Open"), null=False, blank=False)
	submission_1_close = models.DateField(verbose_name=_("Submission 1 Close"), null=False, blank=False)

	review_open = models.DateField(verbose_name=_("Review Open"), null=False, blank=False)
	review_close = models.DateField(verbose_name=_("Review Close"), null=False, blank=False)
	
	submission_2_open = models.DateField(verbose_name=_("Submission 2 Open"), null=False, blank=False)
	submission_2_close = models.DateField(verbose_name=_("Submission 2 Close"), null=False, blank=False)

	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def stage(self):
		now = datetime.date.today()
		if now < self.submission_1_open:
			return {'type': 'before_period', 'text': _('Before the period')}
		elif self.submission_1_open <= now <= self.submission_1_close:
			return {'type': 'submission_open', 'text': _('Submission open')}
		elif self.submission_1_close < now < self.review_open:
			return {'type': 'submission_close', 'text': _('Submission close')}
		elif self.review_open <= now <= self.review_close:
			return {'type': 'reviewing', 'text': _('Reviewing...')}
		elif self.review_close < now < self.submission_2_open:
			return {'type': 'reviewed', 'text': _('Reviewed!')}
		elif self.submission_2_open <= now <= self.submission_2_close:
			return {'type': 'submission_open', 'text': _('Submission open')}
		elif now > self.submission_2_close:
			return {'type': 'submission_close', 'text': _('Submission close')}
		else:
			return {'type': 'out_of_period', 'text': _('Out of period')}

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Event.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Event, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-date']
		verbose_name = _(u'Event')
		verbose_name_plural = _(u'Event')