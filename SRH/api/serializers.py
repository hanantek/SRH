from rest_framework import serializers
from rest_framework.serializers import Field, RelatedField
from django.utils.dateformat import format
from django.contrib.auth.models import User
from cv.models import PersonalInfo

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

class PersonalInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalInfo
		ordering = ['names']
		fields = ('id','user','names','last_names', 'nationality', 'document_type', \
			'document_number', 'sex', 'civil_state', 'phone', 'mobile', 'birth', 'address', 'image')

class SearchSerializer(serializers.ModelSerializer):
	personales = PersonalInfoSerializer(many=False)

	class Meta:
		model = User
		fields = ('id', 'username','personales')
		depth = 3