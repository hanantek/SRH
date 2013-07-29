from django.views.generic import TemplateView
from serializers import NationalitySerializer, DocumentTypeSerializer, GenderSerializer, CivilStateSerializer
from models import Nationality, DocumentType, Gender, CivilState
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics

# get nationality catalog
class NationalityList(generics.ListCreateAPIView):
	queryset = Nationality.objects.all()
	serializer_class = NationalitySerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

class DocumentTypeList(generics.ListCreateAPIView):
	queryset = DocumentType.objects.all()
	serializer_class = DocumentTypeSerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

class GenderList(generics.ListCreateAPIView):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

class CivilStateList(generics.ListCreateAPIView):
	queryset = CivilState.objects.all()
	serializer_class = CivilStateSerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)