from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import *

class HealthNetRegistration(UserCreationForm):
    hosChoices = (
        ('RG', 'Rochester General'),
        ('SM', 'Strong Memorial'),
        ('HH', 'Highland Hospital'),
    )
    email = forms.EmailField(required=True, max_length=100)
    firstName = forms.CharField(required=True, max_length=50)
    lastName = forms.CharField(required=True, max_length=50)
    dob = forms.DateField(required=True)
    phone = forms.IntegerField(required=True)
    ID = forms.CharField(required=True, max_length=15)
    username = forms.CharField(required=True, max_length=20)
    #password = forms.CharField(required=True, max_length=20)
    prefHos = forms.ChoiceField(hosChoices)
    efirstName = forms.CharField(required=True, max_length=50)
    elastName = forms.CharField(required=True, max_length=50)
    ePhone = forms.IntegerField(required=True)
    allergies = forms.CharField(required=True, max_length=300)
    recentOps = forms.CharField(required=True, max_length=300)
    gender = forms.CharField(required=True, max_length=1)
    prescriptions = forms.CharField(required=True, max_length=300)
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'dob', 'phone', 'email', 'ID', 'username', 'prefHos', 'efirstName', 'elastName', 'ePhone', 'allergies', 'recentOps', 'gender', 'prescriptions')

    def save(self, commit=True):
        user = super(HealthNetRegistration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.dob = self.cleaned_data['dob']
        user.phone = self.cleaned_data['phone']
        user.ID = self.cleaned_data['ID']
        user.username = self.cleaned_data['username']
        #user.password = self.cleaned_data['password']
        user.prefHos = self.cleaned_data['prefHos']
        user.efirstName = self.cleaned_data['efirstName']
        user.elastName = self.cleaned_data['elastName']
        user.ePhone = self.cleaned_data['ePhone']
        user.allergies = self.cleaned_data['allergies']
        user.recentOps = self.cleaned_data['recentOps']
        user.gender = self.cleaned_data['gender']
        user.prescriptions = self.cleaned_data['prescriptions']
        if commit:
            user.save()

        return user
