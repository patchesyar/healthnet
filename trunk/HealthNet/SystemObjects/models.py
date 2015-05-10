from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class DoctorManager(models.Manager):

    def create_doctor(self, hospital, user):
        doc = self.create(user=user)
        doc.hospital.add(hospital)
        return doc

class NurseManager(models.Manager):

    def create_nurse(self, user, hospital):
        nurse = self.create(user=user)
        nurse.hospital.add(hospital)
        return nurse

class AdminManager(models.Manager):

    def create_admin(self, user, hospital):
        admin = self.create(user=user)
        admin.hospital.add(hospital)
        return admin

class PatientManager(models.Manager):

    def create_patient(self, user, phone, insuranceID,
                       emergencyFirstName, emergencyLastName, emergencyPhone,
                       sex):
        patient = self.create(user=user)
        patient.phone = phone
        patient.insuranceID = insuranceID
        patient.emergencyFirstName = emergencyFirstName
        patient.emergencyLastName = emergencyLastName
        patient.emergencyPhone = emergencyPhone
        patient.sex = sex
        return patient

class Doctor(models.Model):
    """
    Doctor extends user
    Attributes:
         patient list
    """
    user = models.OneToOneField(User)
    hospital = models.ManyToManyField(Hospital)
    verified = models.BooleanField(blank=False, default=False)
    objects = DoctorManager()

    def verify(self):
        "Edits the boolean field inside the doctor obj to reflect verification"
        self.verified = True
        self.save()

    def __str__(self):
        "returns string of doctor's name"
        return self.user.first_name + " " + self.user.last_name

class Nurse(models.Model):
    """
    Nurse extends user
    Attributes:
        specialization (the word "type" was a python keyword)
    """
    user = models.OneToOneField(User)
    specialization = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)
    verified = models.BooleanField(blank=False, default=False)
    objects = NurseManager()

    def verify(self):
        self.verified = True
        self.save()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Administrator(models.Model):
    """
    According to the Static UML, admin extends user. Considering these will be superusers, I don't know if self makes too much sense - mike.
    """
    user = models.OneToOneField(User)
    hospital = models.ForeignKey(Hospital)
    verified = models.BooleanField(blank=False, default=False)
    objects = AdminManager()

    def verify(self):
        self.verified = True
        self.save()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Patient(models.Model):
    """
    Patient extends user
    """
    user = models.OneToOneField(User)
    associated_doctor = models.ForeignKey(Doctor, null=True)
    hospital = models.ForeignKey(Hospital, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=False)
    insuranceID = models.CharField(max_length=15, blank=False)
    emergencyFirstName = models.CharField(max_length=50, blank=False)
    emergencyLastName = models.CharField(max_length=50, blank=False)
    emergencyPhone = models.CharField(max_length=12, blank=False)
    #emergencyContact = models.ForeignKey('Patient', required=True)
    sex = models.CharField(max_length=6, blank=False)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    objects = PatientManager()
    


class AppointmentManager(models.Manager):
    def create_appointment(self, patient, doctor, time):
        appt = self.create(Patient=patient, Doctor=doctor, Time=time)
        return appt

    # todo: add validates methods, stop using Ruby name conventions


class Appointment(models.Model):
    """
    Appointments
    Attributes:
        people
        time
    """
    Doctor = models.ForeignKey(Doctor)
    Patient = models.ForeignKey(Patient)
    Time = models.DateTimeField()
    objects = AppointmentManager()

    # ToString method:
    def __str__(self):
        return self.Doctor.last_name + " " + self.Patient.last_name

