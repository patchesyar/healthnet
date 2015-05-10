from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import *
from SystemObjects.models import LogEntry, Hospital, Doctor, Patient, Nurse
from django.db import models


class PatientReg1(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=100)
    password1 = forms.CharField(required=True, min_length=8, max_length=64, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, min_length=8, max_length=64, widget=forms.PasswordInput)

    def clean_password(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise forms.ValidationError("Passwords do not match. Please re-enter your password.")

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User.objects.get(email__iexact=email)
            raise forms.ValidationError("Email already exists!")
        except User.DoesNotExist:
            return email

class PatientReg2(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
    dateOfBirth = forms.DateField(required=True)
    phone = forms.CharField(max_length=12, required=True)
    insuranceID = forms.CharField(max_length=15, required=True)
    sex = forms.CharField(max_length=6, required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)

    #def clean_dob(self):
    #    dateOfBirth = self.cleaned_data['dateOfBirth'].strip()
    #    cleanedDOB = 

class PatientReg3(forms.Form):
    emergencyFirstName = forms.CharField(max_length=50, required=True)
    emergencyLastName = forms.CharField(max_length=50, required=True)
    emergencyPhone = forms.CharField(max_length=12, required=True)

class EmployeeReg(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=100)
    password1 = forms.CharField(required=True, min_length=8, max_length=64, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, min_length=8, max_length=64, widget=forms.PasswordInput)
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
    typeChoices = (("Doctor", "Doctor"), ("Nurse", "Nurse"), ("Administrator", "Administrator"),)
    userType = forms.ChoiceField(choices=typeChoices, required=True)

    def clean_password(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 == p2:
            return p2
        raise forms.ValidationError("Passwords do not match, please re-enter your password.")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email__iexact=email)
            raise forms.ValidationError("Email already exists.")
        except User.DoesNotExist:
            return email

class UProfileUpdate(forms.Form):
    last_name = forms.CharField(max_length=50)
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())

class PatientProfileUpdate(UProfileUpdate):
    insuranceID = forms.CharField(max_length=20, required=True)
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all())
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
    phone = forms.CharField(max_length=12)
    weight = forms.IntegerField()
    height = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User.objects.get(email_iexact=email)
            raise forms.ValidationError("Email already exists!")
        except User.DoesNotExist:
            return email
