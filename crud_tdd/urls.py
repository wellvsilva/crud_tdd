from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # urls pessoa
    url(r'^pessoa/add/$', 'core.views.pessoa_add', name='pessoa_add')
)
