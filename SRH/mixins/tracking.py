import datetime
from django.db import models
#from django.contrib.auth.models import User

class TrackingMixin(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True