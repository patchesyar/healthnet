from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import *
from SystemObjects.models import LogEntry


class HealthNetRegistration(UserCreationForm):
    hosChoices = (  # Current list of hospital choices. Change to Foreign key?
        ('RG', 'Rochester General'),
        ('SM', 'Strong Memorial'),
        ('HH', 'Highland Hospital'),
    )
    email = forms.EmailField(required=True, max_length=100)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    dob = forms.DateField(required=True)
    phone = forms.IntegerField(required=True)
    ID = forms.CharField(required=True, max_length=15)
    username = forms.CharField(required=True, max_length=20)
    # password = forms.CharField(required=True, max_length=20)
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
        fields = ('first_name', 'last_name', 'dob', 'phone', 'email', 'ID', 'username', 'prefHos', 'efirstName', 'elastName', 'ePhone', 'allergies', 'recentOps', 'gender', 'prescriptions')

    # Saves the user information into the system
    def save(self, commit=True):  # why is one of our parameters declared here?
        user = super(HealthNetRegistration, self).save(commit=False)  # why is the parameter flipped now?
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.dob = self.cleaned_data['dob']
        user.phone = self.cleaned_data['phone']
        user.ID = self.cleaned_data['ID']
        user.username = self.cleaned_data['username']
        # user.password = self.cleaned_data['password']
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
            print(user)
            log_newUser = LogEntry(actor="System", entryType="New User", details=user.username + " created.")
            log_newUser.save()

        return user
