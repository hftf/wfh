from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from spoticle import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spoticle.views.home', name='home'),
    # url(r'^spoticle/', include('spoticle.foo.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^play/$', views.index, name='play'),
    url(r'^compose/$', views.compose, name='compose'),
    url(r'^random/$', views.random, name='random'),
    url(r'^play/(?P<pk>\d+)/$', views.DetailView.as_view(), name='quiz'),
    url(r'^compose/(?P<pk>\d+)/$', views.UpdateView.as_view()),

    url(r'^clip/(?P<clip_id>\d+)/$', views.clip, name='clip'),

    # Auth
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', { 'template_name': 'login.html', 'extra_context': { 'next': '/' }}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/' }, name='logout'),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
