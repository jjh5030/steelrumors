from django.conf.urls import patterns, include, url
from links.views import LinkListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include('profiles.urls')),
)
