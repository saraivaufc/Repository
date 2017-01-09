from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Keyword(models.Model):
	FIELDS_SEARCH = (
		("name", _("Name")),
	)
	name = models.CharField(verbose_name=_("Name"), max_length=100, null=False, blank=False, unique=True)
	slug = models.SlugField(verbose_name=_('slug'), max_length=60, blank=True, unique=True)
	
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)


	def save(self, *args, **kwargs):
		if not self.id:
			self.name = self.name.upper()
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Keyword.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Keyword, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def verbose_name(self):
		return self._meta.verbose_name

	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Keyword")
		verbose_name_plural = _(u"Keywords")