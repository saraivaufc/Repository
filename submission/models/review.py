from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Review(models.Model):
	slug = models.SlugField(verbose_name=_('Slug'), max_length=500, blank=True, unique=True)
	review_available_in = models.BooleanField(default=False, verbose_name=_(u"Review Available"))
	
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