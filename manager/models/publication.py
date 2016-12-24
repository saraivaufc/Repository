from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db import models
from authentication.models import Profile
import itertools

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

class Publication(models.Model):
	title = models.CharField(verbose_name=_("Title"), max_length=500, null=False, blank=False)
	slug = models.SlugField(_('slug'), max_length=60, blank=True, unique=True)
	typology = models.CharField(verbose_name=_("Typology"), choices=TYPOLOGY_CHOICES, max_length=100, null=False, blank=False)
	subjects = models.ManyToManyField("Subject", verbose_name=_("Subjects"), null=False, blank=False)
	authors = models.ManyToManyField("Author", verbose_name=_("Authors"), related_name=_("Authors"), null=False, blank=False)
	advisors = models.ManyToManyField("Author", verbose_name=_("Advisors"), related_name=_("Advisors"), null=True, blank=True)
	collection = models.ForeignKey("Collection", verbose_name=_("Collection"), null=False, blank=False)
	publisher = models.ForeignKey("Publisher", verbose_name=_("Publisher"), null=True, blank=True)
	address = models.CharField(verbose_name=_("Address"), max_length=100, null=False, blank=False)
	year = models.IntegerField(verbose_name=_("Year"), null=False, blank=False)
	reference = models.CharField(verbose_name=_("Reference"), max_length=1000, null=False, blank=False)
	uri = models.URLField(verbose_name=_("URI"), max_length=500, null=False, blank=True)
	language = models.CharField(verbose_name=_("Language"), choices=LANGUAGE_CHOICES, max_length=100, null=False, blank=False)
	abstract = models.TextField(verbose_name=_("Abstract"), null=False, blank=False)
	other_abstract = models.TextField(verbose_name=_("Other Abstract"), null=True, blank=True)
	keywords = models.ManyToManyField("KeyWord", verbose_name=_("Keywords"), related_name=_("Keywords"), null=False, blank=False)
	issue_date = models.DateField(verbose_name=_("Issue Date"), null=False, blank=False, auto_now=False)
	file = models.FileField(verbose_name=_(u"File"), upload_to='documents/publication/%Y/%m/%d', null=False, blank=False)
	
	registration_date = models.DateTimeField(verbose_name=_("Registration Date"), auto_now_add=True, auto_now=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = orig = slugify(self.title)
			for x in itertools.count(1):
				if not Publication.objects.filter(slug=self.slug).exists():
					break
				self.slug = "%s-%d" % (orig, x)
		self.uri = "http://www.google.com"
		super(Publication, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-registration_date']
		verbose_name = _(u"Publication")
		verbose_name_plural = _(u"Publications")