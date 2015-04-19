from django.db import models
from datetime import *

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthNet.settings")

# The following unused imports were removed in the R1 refactor:
# from calendar import HTMLCalendar
# from datetime import date
# from itertools import groupby
# from django.utils.html import conditional_escape as esc

# Create your models here.


class Message(models.Model):  # models.Model superclass
    """
    self class is the blueprint for message objects
    Attributes:
        Title
        Message
        Recipient
        Sender
    """
    title = models.CharField(max_length=500)  # 500 for a title seems good?
    message = models.CharField(max_length=2000)  # not sure how 2000 will work out

    """These attributes will need to take a User object - not quite sure how to do this right now"""
    recipient = None  # change to a user object somehow
    sender = None  # change to a user object somehow

    # ToString method:
    def __str__(self):
        return self.title


# LogEntry has its own data table in the SQL file
class LogEntry(models.Model):
    """
    LogEntry
    Attributes:
        time
        actor
        target
        type
        details
    """
    time = models.DateTimeField(default=datetime.now())
    actor = models.CharField(max_length=50, default="[User Type and Name]")
    entryType = models.CharField(max_length=50, default="[Event]")  # TODO: Change to enumerator
    details = models.TextField(max_length=200, default="[Event Details]")  # Determine suitable max length

    # ToString method:
    def __str__(self):
        return self.details  # want to see the details or something else? TODO: Pick one
        # return self.time #could see this instead if we want


class Hospital(models.Model):
    """
    Hospital
    Attributes:
        name
        address
        admins
        doctors
        nurses
        patients
        log
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    admins = []  # list of admin objects
    doctors = []  # list of doctor objects
    nurses = []  # list of nurse objects
    patients = []  # list of patient objects

    # ToString method:
    def __str__(self):
        return self.name


class User(models.Model):  # superclass is models.Model (i think) -mike
    """
    this is the parent class for all types of users
    any attributes or methods that belong to all users should go here.
    Attributes:
        First name
        Last name
    """

    # Here are the attributes for the names

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    messages = []  # list of message objects
    appointments = []  # list of appointment objects
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    insurance = models.CharField(max_length=100)

    # ToString method:
    def __str__(self):
        return self.first_name + " " + self.last_name


class Doctor(User):  # inherits from User
    """
    Doctor extends user
    Attributes:
         patient list
    """
    patients = []  # list of patients
    hospital = models.ForeignKey(Hospital)


class Nurse(User):
    """
    Nurse extends user
    Attributes:
        specialization (the word "type" was a python keyword)
    """
    specialization = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)


class Administrator(User):
    """
    According to the Static UML, admin extends user. Considering these will be superusers, I don't know if self makes too much sense - mike.
    """
    hospital = models.ForeignKey(Hospital)


class Patient(User):
    """
    Patient extends user
    """
    prescriptions = None  # One to many relationship with prescription objects
    associated_doctor = models.ForeignKey(Doctor)
    hospital = models.ForeignKey(Hospital)


class Appointment(models.Model):
    """
    Appointments
    Attributes:
        people
        time
    """
    Doctor = models.ForeignKey(Doctor)
    Patient = models.ForeignKey(Patient)
    time = models.DateTimeField()

    # ToString method:
    def __str__(self):
        return self.Doctor.last_name + " " + self.Patient.last_name
