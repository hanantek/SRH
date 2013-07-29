from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SRH.views.home', name='home'),
    # url(r'^SRH/', include('SRH.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'i18n/', include('django.conf.urls.i18n')),
    url(r'', include('cv.urls')),
    url(r'', include('catalog.urls')),
    url(r'', include('api.urls')),
    url(r'^reportes/', include('reportes.urls')),
    #url(r'', include('social_auth.urls')),
    #url(r'^login/$', RedirectView.as_view(url='/login/facebook/')),
    url(r'^accounts/', include('allauth.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )

