from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from views import NationalityList, DocumentTypeList, GenderList, CivilStateList

urlpatterns = patterns('',
    url(r'^api/v1.0/nationality/$', NationalityList.as_view(), name='nationality-list'),
    url(r'^api/v1.0/document/$', DocumentTypeList.as_view(), name='document-list'),
    url(r'^api/v1.0/gender/$', GenderList.as_view(), name='gender-list'),
    url(r'^api/v1.0/civilstate/$', CivilStateList.as_view(), name='civilstate-list'),
)