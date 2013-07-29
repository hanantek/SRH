from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from views import PersonalInfoList, PersonalInfoDetail,\
                     CurrentUser, PersonalViewSet, SearchResults
router = DefaultRouter()
router.register(r'personal', PersonalViewSet)

urlpatterns = patterns('',
	url(r'^api/v1.0/', include(router.urls)),
	url(r'^api/v1.0/user/$', CurrentUser.as_view(), name='current-user'),
    url(r'^api/v1.0/personalinfo/$', PersonalInfoList.as_view(), name='personal-list'),
    url(r'^api/v1.0/personalinfo/(?P<pk>[0-9]+)/$', PersonalInfoDetail.as_view(), name='personal-detail'),
    url(r'^api/v1.0/search/$', SearchResults.as_view(), name='search'),
)