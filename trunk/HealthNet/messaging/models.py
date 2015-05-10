from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	sentby = models.ForeignKey(User, related_name='userwhosent')
	sentto = models.ForeignKey(User, related_name='userwhogot')
	timesent = models.DateTimeField("Time sent")
	subject = models.CharField(max_length = 128)
	message = models.CharField(max_length = 4096)
	def __str__(self):
		return sentby.username + " to " + sentto.username + " at "\
				+ str(timesent)
