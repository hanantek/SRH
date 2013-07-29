from rest_framework import serializers
from rest_framework.serializers import Field, RelatedField
from django.utils.dateformat import format
from models import Nationality, DocumentType, Gender, CivilState

class NationalitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Nationality
		ordering = ['name']
		fields = ('id','name')

class DocumentTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = DocumentType
		ordering = ['id']
		fields = ('id', 'document')

class GenderSerializer(serializers.ModelSerializer):
	gender = serializers.Field(source='get_gender_display')
	
	class Meta:
		model = Gender
		ordering = ['id']
		fields = ('id', 'gender')

class CivilStateSerializer(serializers.ModelSerializer):
	class Meta:
		model = CivilState
		ordering = ['id']
		fields = ('id', 'state')