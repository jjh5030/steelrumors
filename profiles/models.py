from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	bio = models.TextField(null=True)

	def __unicode__(self):
		return "%s's profile" % self.user