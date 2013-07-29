from django.db import models
from django.utils.translation import ugettext_lazy as _
from mixins.tracking import TrackingMixin

# models for catalogs

class Nationality(TrackingMixin):
	name = models.CharField(max_length=50, verbose_name=_('Nationality'))

	class Meta:
		verbose_name = _('Nationality')
		verbose_name_plural = _('Nationalities')

	def __unicode__(self):
		return u'%s' % self.name

class DocumentType(TrackingMixin):
	document = models.CharField(max_length=50, verbose_name=_('Document'))

	class Meta:
		verbose_name = _('Document type')
		verbose_name_plural = _('Document types')

	def __unicode__(self):
		return u'%s' % self.document

class Gender(TrackingMixin):
	GENDER_CHOICES = (
		('M', _('Male')),
		('F', _('Female')),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))

	class Meta:
		verbose_name = _('Gender')
		verbose_name_plural = _('Genders')

	def __unicode__(self):
		return u'%s' % self.get_gender_display()

class CivilState(TrackingMixin):
	state = models.CharField(max_length=100, verbose_name=_('State'))

	class Meta:
		verbose_name = _('Civil state')
		verbose_name_plural = _('Civil states')

	def __unicode__(self):
		return u'%s' % self.state