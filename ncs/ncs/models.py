from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
	name = models.CharField(required = False)
	createdAt = models.DateField(default=datetime.date.today)
	assignedAt = models.CharField(default=datetime.date.today)
	count = models.IntField(required = True)