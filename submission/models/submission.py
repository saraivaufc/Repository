from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
from django.conf import settings
import itertools

from manager.models import Publication
from authentication.models import User

class Submission(models.Model):
	FIELDS_SEARCH = (
		("publication.title", _("Title")), 
		("publication.description", _("Description")),
	)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=500, blank=True, unique=True)
	event = models.ForeignKey("Event", verbose_name=_("Event"), null=False, blank=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="User", null=False, blank=False)
	publication = models.ForeignKey(Publication, verbose_name=_("Publication"), null=True, blank=True)
	reviser = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Reviser"), related_name="Reviser", limit_choices_to={'is_reviser': True}, null=True, blank=True)
	review = models.ForeignKey("Review", verbose_name=_("Review"), null=True, blank=True)
	
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.publication.title 

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.event.name + "-" + self.user.get_short_name())
			for x in itertools.count(1):
				if not Submission.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Submission, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		publication = self.publication
		publication.delete()
		super(Submission, self).delete(*args, **kwargs)
	class Meta:
		verbose_name = _(u'Submission')
		verbose_name_plural = _(u'Submission')
		permissions = (
			("list_submission_to_review", "List Submission To  Review"),
			("submit_final", "Submit Final"),
		)