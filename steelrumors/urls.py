from django.conf.urls import patterns, include, url
from links.views import LinkListView, LinkCreateView, LinkDetailView, LinkDeleteView, LinkUpdateView
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^link/create/$', auth(LinkCreateView.as_view()), name='link_create'),
    url(r'^link/update/(?P<pk>\d+)/$', auth(LinkUpdateView.as_view()), name='link_update'),
    url(r'^link/delete/(?P<pk>\d+)/$', auth(LinkDeleteView.as_view()), name='link_delete'),
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(), name='link_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include('profiles.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
