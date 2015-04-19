from django import forms
from django.utils.safestring import *
from SystemObjects.models import LogEntry, Appointment, Patient, Doctor


class apptRegistration(forms.Form):
    Patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    Doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    Time = forms.DateTimeField()


    appointment = Appointment()
    log_newAppt = LogEntry(actor="System", entryType="New Appointment",
                                   details="Appointment Created")
    log_newAppt.save()