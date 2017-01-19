from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
from django.core.urlresolvers import reverse_lazy
import itertools

class Publication(models.Model):
	TYPOLOGY_CHOICES = (
	    (u'article', _(u'Article')),
	    (u'book', _(u'Book')),
	    (u'booklet', _(u'Booklet')),
	    (u'conference', _(u'Conference')),
	    (u'inbook', _(u'Inbook')),
	    (u'incollection', _(u'Incollection')),
	    (u'manual', _(u'Manual')),
	    (u'mastersthesis', _(u'Masters Thesis')),
	    (u'monography', _(u'Monography')),
	    (u'dissertation', _(u'Dissertation')),
	    (u'abstract', _(u'Abstract')),
	)
	LANGUAGE_CHOICES = (
	    (u'pt_BR', _(u'Brazilian Portuguese')),
	    (u'en', _(u'English')),
	 	(u'es', _(u'Spanish')),   
	)
	title = models.CharField(verbose_name=_("Title"), max_length=500, null=False, blank=False)
	slug = models.SlugField(_('slug'), max_length=1000, blank=True, unique=True)
	typology = models.CharField(verbose_name=_("Typology"), choices=TYPOLOGY_CHOICES, max_length=100, null=False, blank=False)
	subjects = models.ManyToManyField("Subject", verbose_name=_("Subjects"), blank=False)
	authors = models.ManyToManyField("Author", verbose_name=_("Authors"), related_name="Authors", blank=False)
	community = models.ForeignKey("Community", verbose_name=_("Community"), null=False, blank=False)
	collection = models.ForeignKey("Collection", verbose_name=_("Collection"), null=False, blank=False)
	publisher = models.ForeignKey("Publisher", verbose_name=_("Publisher"), null=False, blank=False)
	address = models.CharField(verbose_name=_("Address"), max_length=100, null=False, blank=False)
	year = models.IntegerField(verbose_name=_("Year"), null=False, blank=False)
	reference = models.CharField(verbose_name=_("Reference"), max_length=1000, null=False, blank=False)
	uri = models.URLField(verbose_name=_("URI"), max_length=500, null=False, blank=False)
	
	principal_language = models.CharField(verbose_name=_("Principal Language"), choices=LANGUAGE_CHOICES, max_length=100, null=True, blank=True)
	principal_abstract = models.TextField(verbose_name=_("Principal Abstract"), null=True, blank=True)
	principal_keywords = models.ManyToManyField("KeyWord", verbose_name=_("Principal Keywords"), related_name="principal_keywords", blank=True)

	secondary_language = models.CharField(verbose_name=_("Secondary Language"), choices=LANGUAGE_CHOICES, max_length=100, null=True, blank=True)
	secondary_abstract = models.TextField(verbose_name=_("Secondary Abstract"), null=True, blank=True)
	secondary_keywords = models.ManyToManyField("KeyWord", verbose_name=_("Secondary Keywords"), related_name="secondary_keywords", blank=True)
	
	
	issue_date = models.DateField(verbose_name=_("Issue Date"), null=False, blank=False, auto_now=False)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/publication/%Y/%m/%d', null=False, blank=False)
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)
	is_final =  models.BooleanField(verbose_name=_(u"Is Final"), default=False,)

	def get_search_fields():
		return (
			("title", _("Title")),
			("principal_abstract", _("Principal Abstract")),
			("secondary_abstract", _("Secondary Abstract")),
			("year", _("Year")),
		)
	def get_output_fields():
		return (
			("title", _("Title")),
			("typology", _("Typology")), 
			("authors", _("Authors")),
		 	("year", _("Year")),
		)

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.title)
			for x in itertools.count(1):
				if not Publication.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		super(Publication, self).save(*args, **kwargs)

	def get_typology(self):
		for elem in list(self.TYPOLOGY_CHOICES):
			if elem[0] == self.typology:
				return elem[1]
		return self.typology

	def get_principal_language(self):
		for elem in list(self.LANGUAGE_CHOICES):
			if elem[0] == self.principal_language:
				return elem[1]
		return self.principal_language

	def get_secondary_language(self):
		for elem in list(self.LANGUAGE_CHOICES):
			if elem[0] == self.secondary_language:
				return elem[1]
		return self.secondary_language

	def __unicode__(self):
		return self.title

	def natural_key(self):
		return self.title

	def verbose_name(self):
		return self._meta.verbose_name

	def get_absolute_url(self):
		return reverse_lazy('manager:publication_detail', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Publication")
		verbose_name_plural = _(u"Publications")

from django.db.models.signals import post_save
from django.dispatch import receiver

def post_save_receiver(sender, instance, created, ** kwargs):
	if not instance.uri:
		instance.uri = reverse_lazy("manager:publication_uri", kwargs={"pk": instance.pk})
		instance.save()
		
post_save.connect(post_save_receiver, sender=Publication)
