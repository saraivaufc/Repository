from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Review(models.Model):
	LEVEL = (
		("Bad", _("Bad")),
		("Fragile", _("Fragile")),
		("Average", _("Average")),
		("Good", _("Good")),
		("Fantastic", _("Fantastic")),
	)

	originality = models.CharField(verbose_name=_("Originality"), max_length=100, choices=LEVEL, null=False, blank=False)
	originality_observation = models.TextField(verbose_name=_("Originality observation"), null=True, blank=True)

	technical_merit = models.CharField(verbose_name=_("Technical Merit"), max_length=100, choices=LEVEL, null=False, blank=False)
	technical_merit_observation = models.TextField(verbose_name=_("Technical Merit observation"), null=True, blank=True)

	clarity = models.CharField(verbose_name=_("Clarity"), max_length=100, choices=LEVEL, null=False, blank=False)
	clarity_observation = models.TextField(verbose_name=_("Clarity observation"), null=True, blank=True)

	text_quality = models.CharField(verbose_name=_("Text Quality"), max_length=100, choices=LEVEL, null=False, blank=False)
	text_quality_observation = models.TextField(verbose_name=_("Text Quality Observation"), null=True, blank=True)

	relevance = models.CharField(verbose_name=_("Relevance"), max_length=100, choices=LEVEL, null=False, blank=False)
	relevance_observation = models.TextField(verbose_name=_("Relevance Observation"), null=True, blank=True)

	knowledge_level_revisor = models.CharField(verbose_name=_("Knowledge Level Revisor"), max_length=100, choices=LEVEL, null=False, blank=False)
	knowledge_level_revisor_observation = models.TextField(verbose_name=_("Knowledge Level Revisor Observation"), null=True, blank=True)

	general = models.CharField(verbose_name=_("General"), max_length=100, choices=LEVEL, null=False, blank=False)
	general_observation = models.TextField(verbose_name=_("General Observation"), null=True, blank=True)

	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return str(_("Review"))