from django.db import models
from django_countries import CountryField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from mixins.tracking import TrackingMixin
from catalog.models import Nationality, DocumentType, Gender, CivilState
# Model for store personal info form user
class PersonalInfo(TrackingMixin):
	user = models.OneToOneField(User, verbose_name=_('User'), related_name="personales")
	names = models.CharField(max_length=150, verbose_name=_('Names'))
	last_names = models.CharField(max_length=150, verbose_name=_('Last names'))
	nationality = models.ForeignKey(Nationality, verbose_name=_('Nationality'))
	document_type = models.ForeignKey(DocumentType, verbose_name=_('Document type'))
	document_number = models.CharField(max_length=20, verbose_name=_('Document number'))
	sex = models.ForeignKey(Gender, verbose_name=_('Gender'))
	civil_state = models.ForeignKey(CivilState, verbose_name=_('Civil state'))
	phone = models.CharField(max_length=30, verbose_name=_('Phone'))
	mobile = models.CharField(max_length=30, verbose_name=_('Mobile'))
	birth = models.DateField(verbose_name=_('Birth date'))
	address = models.CharField(max_length=250, verbose_name=_('Address'))
	image = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name=_('Image'))

	class Meta:
		verbose_name = _('Personal Info')
		verbose_name_plural = _('Personal Infos')

	def __unicode__(self):
		return u'%s %s' % (self.names, self.last_names)