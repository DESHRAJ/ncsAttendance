from django.db import models
import datetime

class ncsMembers(models.Model):
	name = models.CharField(max_length = 1000)
	createdAt = models.DateField(default=datetime.date.today )
	markedAt = models.DateField()
	count = models.CharField(max_length = 1000)
	club = models.CharField(max_length = 500)

