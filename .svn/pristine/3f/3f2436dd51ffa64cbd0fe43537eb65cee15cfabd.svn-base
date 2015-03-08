from django.db import models

#thing team selfie added
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthNet.settings")


# Create your models here.

class Message(models.Model):#models.Model superclass
    """
    self class is the blueprint for message objects
    Attributes:
        Title
        Message
        Recipient
        Sender
    """
    title = models.CharField(max_length=500)#500 for a title seems good?
    message = models.CharField(max_length=2000)#not sure how 2000 will work out

    """These attributes will need to take a User object - not quite sure how to do this right now"""
    recipient = None #change to a user object somehow
    sender = None #change to a user object somehow

    #ToString method:
    def __str__(self):
        return self.title
    
class Appointment(models.Model):
    """
    Appointments
    Attributes:
        people
        time
    """
    people = []#list of Users
    time = None#not sure if this should be an int or what... - mike

    #ToString method:
    def __str__(self):
        return self.time #maybe we could think of something a little more descriptive

class Log(models.Model):
    """
    Logs
        Attributes:
        logs
    """
    logs = []#list of "LogEntry" objects

    #ToString method: Commented out b/c it doesn't seem to be that necessary or descriptive
    #def __str__(self):
        #return self.logs

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
    time = None#DateTime object
    actor = None#User object
    target = None#!!!!!!!the static uml says "Object"!!??!??!?! what even is this???????????
    entryType = None#couldn't use "type" on account of it being a keyword for python; string
    details = models.CharField(max_length=500)#500? or how much room for details is needed?

    #ToString method:
    def __str__(self):
        return self.details #want to see the details or something else?
        #return self.time #could see this instead if we want
        

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
    address = models.CharField(max_length=500)#500 should be enough for an address i think - mike.
    admins = []#list of admin objects
    doctors = []#list of doctor objects
    nurses = []#list of nurse objects
    patients = []#list of patient objects
    log = None#According to the static uml, this should be a "Log" object

    #ToString method:
    def __str__(self):
        return self.name

class User(models.Model):#superclass is models.Model (i think) -mike
    """
    this is the parent class for all types of users
    any attributes or methods that belong to all users should go here.
    Attributes:
        First name
        Last name
    """
    
    #Here are the attributes for the names
    
    first_name = models.CharField(max_length=200)#200 char length seems good enough
    last_name = models.CharField(max_length=200)#no camelCase for underscore names??
    messages = []#list of message objects
    appointments = []#list of appointment objects
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)

    #ToString method:
    def __str__(self):
        return self.first_name +" "+self.last_name #I have this set to display the whole name of person

class Doctor(User):#inherits from User??
    """
    Doctor extends user
    Attributes:
         patient list   
    """
    patients = []#list of patients
    hospital = models.ForeignKey(Hospital)

class Nurse(User):
    """
    Nurse extends user
    Attributes:
        specialization (the word "type" was a python keyword)
    """
    specialization = models.CharField(max_length=200) #string defining type of Nurse - i assume this will be somewhat optional
    hospital = models.ForeignKey(Hospital)

class Admin(User):
    """
    According to the Static UML, admin extends user. Considering these will be superusers, I don't know if self makes too much sense - mike.
    """
    hospital = None#should be a hospital object
    
class Patient(User):
    """
    Patient extends user
    """
    prescriptions = None#list of prescription objects
    associated_doctor = models.ForeignKey(Doctor)#doctor object
    hospital = models.ForeignKey(Hospital)
