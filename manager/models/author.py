from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.db import models
import itertools


class Author(models.Model):
	
	first_name = models.CharField(verbose_name=_("First name"), max_length=100, null=False, blank=False)
	last_name = models.CharField(verbose_name=_("Last name"), max_length=100, null=False, blank=False)
	reference_name = models.CharField(verbose_name=_("Reference name"), max_length=200, null=True, blank=True)
	slug = models.SlugField(verbose_name=_('slug'), max_length=60, blank=True, unique=True)

	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)
	
	def get_search_fields():
		return (
			("first_name", _("First Name")), 
			("last_name", _("Last Name")),
		)
	def get_output_fields():
		return (
			("first_name", _("First Name")), 
			("last_name", _("Last Name")),
			("reference_name", _("Reference name")),
		)

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify("%s-%s" % (self.first_name, self.last_name) )
			for x in itertools.count(1):
				if not Author.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		self.reference_name = self.last_name.upper() + ", " + self.first_name
		super(Author, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.reference_name

	def natural_key(self):
		return self.reference_name

	def verbose_name(self):
		return self._meta.verbose_name

	def get_absolute_url(self):
		return reverse_lazy('manager:author_detail', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Author")
		verbose_name_plural = _(u"Authors")