from django.db import models
from django.contrib.auth.models import User
import datetime

class userDetails(models.Model):
	name = models.CharField(max_length = 1000)
	createdAt = models.DateField(default=datetime.date.today)
	assignedAt = models.CharField(default=datetime.date.today)
	count = models.CharField(max_length = 1000)