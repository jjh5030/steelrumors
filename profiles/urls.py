from django.conf.urls import patterns, include, url
from profiles.views import UserProfileDetailView, UserProfileEditView

from django.contrib.auth.decorators import login_required as auth

urlpatterns = patterns('',
	url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='profile'),    
)
