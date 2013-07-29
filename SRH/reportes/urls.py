from django.conf.urls import patterns, include, url
from views import HomeView, Profile

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='reportes'),
    url(r'^perfil/(?P<id>\d+)/$', Profile.as_view(), name='profile'),
) 