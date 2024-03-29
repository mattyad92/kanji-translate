from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kanjitranslate.ktranslator.views.home', name='home'),
    url(r'^login/(?P<login_id>\d+)/$', 'kanjitranslate.ktranslator.views.detail'),
    # url(r'^kanjitranslate/', include('kanjitranslate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^ktranslator/$', 'ktranslator.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

urlpatterns += staticfiles_urlpatterns()
