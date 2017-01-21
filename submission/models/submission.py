from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.conf import settings
import itertools

from manager.models import Publication
from authentication.models import User

class Submission(Publication):
	event = models.ForeignKey("Event", verbose_name=_("Event"), null=False, blank=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), related_name="User", null=False, blank=False)
	reviser = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Reviser"), related_name="Reviser", limit_choices_to={'is_reviser': True}, null=True, blank=True)
	review = models.ForeignKey("Review", verbose_name=_("Review"), null=True, blank=True)
	
	def get_search_fields():
		return (
			("title", _("Title")),
		)
	def get_output_fields():
		return (
			("event", _("Event")),
			("user", _("User")),
			("reviser", _("Reviser")),
		)

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify("%s-%s" % (self.event.name, self.user.get_short_name(), ))
			for x in itertools.count(1):
				if not Submission.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Submission, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	def natural_key(self):
		return self.title

	def verbose_name(self):
		return self._meta.verbose_name

	def get_absolute_url(self):
		return reverse_lazy('submission:submission_detail', kwargs={'event_slug': self.event.slug, 'slug': self.slug})

	class Meta:
		verbose_name = _(u'Submission')
		verbose_name_plural = _(u'Submission')
		permissions = (
			("list_submission_to_review", "List Submission To  Review"),
			("detail_submission_to_review", "Detail Submission To Review"),
			("submit_final", "Submit Final"),
		)