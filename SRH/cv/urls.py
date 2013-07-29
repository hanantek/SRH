from django.conf.urls import patterns, include, url
from views import HomeView, IndexView

urlpatterns = patterns('',
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^$', IndexView.as_view(), name='index'),
) 