from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # urls pessoa
    url(r'^pessoa/add/$', 'core.views.pessoa_add', name='pessoa_add'),
    url(r'^pessoa/save/(?P<pk>\d+)/$', 'core.views.pessoa_save', name='pessoa_save'),
    url(r'^pessoa/delete/(?P<pk>\d+)/$', 'core.views.pessoa_delete', name='pessoa_delete'),

)
