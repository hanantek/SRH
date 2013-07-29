from serializers import PersonalInfoSerializer, SearchSerializer
from cv.models import PersonalInfo
from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User


class CurrentUser(APIView):
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)

# get list of personal info

class SearchResults(generics.ListAPIView):
	serializer_class = SearchSerializer
	
	def get_queryset(self):
		queryset = User.objects.all()
		industry = self.request.QUERY_PARAMS.get('industria', None)
		if industry is not None:
			queryset = queryset.filter(experiencias__industry=industry)
		nationality = self.request.QUERY_PARAMS.get('nacionalidad', None)
		if nationality is not None:
			queryset = queryset.filter(personales__nationality=nationality)
		document_type = self.request.QUERY_PARAMS.get('tipo-documento', None)
		if document_type is not None:
			queryset = queryset.filter(personales__document_type=document_type)
		civil_state = self.request.QUERY_PARAMS.get('estado-civil', None)
		if civil_state is not None:
			queryset = queryset.filter(personales__civil_state=civil_state)
		level_education = self.request.QUERY_PARAMS.get('nivel-educacion', None)
		if level_education is not None:
			queryset = queryset.filter(formaciones__level_education=level_education)
		names = self.request.QUERY_PARAMS.get('nombres', None)
		if names is not None:
			queryset = queryset.filter(personales__names__contains=names)
		last_names = self.request.QUERY_PARAMS.get('apellidos', None)
		if last_names is not None:
			queryset = queryset.filter(personales__last_names__contains=names)
		institution = self.request.QUERY_PARAMS.get('institucion', None)
		if institution is not None:
			queryset = queryset.filter(formaciones__institution__contains=institution)
		position = self.request.QUERY_PARAMS.get('posicion', None)
		if position is not None:
			queryset = queryset.filter(experiencias__position__contains=position)
		company = self.request.QUERY_PARAMS.get('empresa', None)
		if company is not None:
			queryset = queryset.filter(experiencias__company__contains=company)
		return queryset

class PersonalViewSet(viewsets.ModelViewSet):
	queryset = PersonalInfo.objects.all()
	serializer_class = PersonalInfoSerializer
	filter_fields = ('user',)
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

class PersonalInfoList(generics.ListCreateAPIView):
	queryset = PersonalInfo.objects.all()
	serializer_class = PersonalInfoSerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)
	filter_fields = ('user',)

# get a object personal info
class PersonalInfoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PersonalInfo.objects.all()
	serializer_class = PersonalInfoSerializer
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)
	filter_fields = ('user',)