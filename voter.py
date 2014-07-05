import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'steelrumors.settings')
from links.models import Link, Vote
from django.contrib.auth.models import User

a = User.objects.all()[0]

for i in xrange(100): 
	Vote(link=Link.objects.order_by('?')[0],voter=a).save()