from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    UserProfile is a representation of a system user. They have many attributes, all shown as fields here
    """
    # User Information
    user = models.OneToOneField(User)
    insuranceid = models.IntegerField()
    hospital = models.CharField(max_length=50)
    birthday = models.DateField()
    phone = models.IntegerField()  # TODO: Change this to only accept 10-digit numbers
    # Emergency Contact Information
    emergency_firstname = models.CharField(max_length=50)
    emergency_lastname = models.CharField(max_length=50)
    emergency_phone = models.IntegerField()  # TODO: Change this to only accept 10-digit numbers
    # Medical Information
    allergies = models.CharField(max_length=300)
    recent_operations = models.CharField(max_length=300)
    gender = models.CharField(max_length=1)
    prescriptions = models.CharField(max_length=300)
