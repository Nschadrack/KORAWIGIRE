from datetime import datetime
from django.db import models


class ContactMessage(models.Model):
	full_name = models.CharField(max_length=60)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField()
	date_created = models.DateTimeField(default=datetime.utcnow)



	def __str__(self):
		return self.message