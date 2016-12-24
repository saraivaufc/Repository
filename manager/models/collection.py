from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Collection(models.Model):
	community = models.ForeignKey("Community", verbose_name=_("Community"), null=False, blank=False)
	name = models.CharField(verbose_name=_("Name"), max_length=100, null=False, blank=False)
	description = models.TextField(verbose_name=_("description"), null=False, blank=False)
	slug = models.SlugField(verbose_name=_('slug'), max_length=60, blank=True, unique=True)
	
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Collection.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)		
		super(Collection, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.community) + " - " + self.name

	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Collection")
		verbose_name_plural = _(u"Collection")