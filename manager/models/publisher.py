from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
import itertools

class Publisher(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=100, unique=True, null=False, blank=False)
	slug = models.SlugField(_('slug'), max_length=60, blank=True, unique=True)
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def get_search_fields():
		return (("name", _("Name")),)
	def get_output_fields():
		return (("name", _("Name")),)
	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.name)
			for x in itertools.count(1):
				if not Publisher.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Publisher, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	def natural_key(self):
		return self.name

	def verbose_name(self):
		return self._meta.verbose_name
	
	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Publisher")
		verbose_name_plural = _(u"Publishers")
