from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Review(models.Model):
	LEVEL = (
		("bad", _("Bad")),
		("fragile", _("Fragile")),
		("average", _("Average")),
		("Good", _("Good")),
		("fantastic", _("Fantastic")),
	)

	slug = models.SlugField(verbose_name=_('Slug'), max_length=500, blank=True, unique=True)

	originality = models.CharField(verbose_name=_("Originality"), max_length=100, choices=LEVEL, null=False, blank=False)
	originality_observation = models.TextField(verbose_name=_("Originality observation"), max_length=200, null=True, blank=True)

	technical_merit = models.CharField(verbose_name=_("Technical Merit"), max_length=100, choices=LEVEL, null=False, blank=False)
	technical_merit_observation = models.TextField(verbose_name=_("Technical Merit observation"), max_length=200, null=True, blank=True)

	clarity = models.CharField(verbose_name=_("Clarity"), max_length=100, choices=LEVEL, null=False, blank=False)
	clarity_observation = models.TextField(verbose_name=_("Clarity observation"), max_length=200, null=True, blank=True)

	text_quality = models.CharField(verbose_name=_("Text Quality"), max_length=100, choices=LEVEL, null=False, blank=False)
	text_quality_observation = models.TextField(verbose_name=_("Text Quality Observation"), max_length=200, null=True, blank=True)

	relevance = models.CharField(verbose_name=_("Relevance"), max_length=100, choices=LEVEL, null=False, blank=False)
	relevance_observation = models.TextField(verbose_name=_("Relevance Observation"), max_length=200, null=True, blank=True)

	knowledge_level_revisor = models.CharField(verbose_name=_("Knowledge Level Revisor"), max_length=100, choices=LEVEL, null=False, blank=False)
	knowledge_level_revisor_observation = models.TextField(verbose_name=_("Knowledge Level Revisor Observation"), max_length=200, null=True, blank=True)

	general = models.CharField(verbose_name=_("General"), max_length=100, choices=LEVEL, null=False, blank=False)
	general_observation = models.TextField(verbose_name=_("General Observation"), max_length=200, null=True, blank=True)

	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.slug

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.review_available_in)
			for x in itertools.count(1):
				if not Review.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Review, self).save(*args, **kwargs)