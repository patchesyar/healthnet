from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
#from login.forms import HealthNetRegistration
from django.contrib.auth.decorators import login_required
from SystemObjects.models import LogEntry
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.auth.models import User
from SystemObjects.models import Patient, Doctor, Nurse, Administrator

# The following imports have been removed during R1 Code Refactoring:
# django.shortcuts.render django.contrib.auth.authenticate django.contrib.auth.login
# django.http.HttpResponse django.db.models django.views.generic django.contrib.auth.forms.UserCreationForm

# Displays user information
@login_required(login_url='/login/')
def account_view(request):
        return render_to_response('account.html',
                                  {
                                      'email': request.user.email,
                                      'first_name': request.user.first_name,
                                      'last_name': request.user.last_name,
                                      'dateOfBirth': request.user.patient.dateOfBirth,
                                      'phone': request.user.patient.phone,
                                      'ID': request.user.patient.insuranceID,
                                      'username': request.user.username,
                                      'hospital': request.user.patient.hospital,
                                      'emergencyFirstName': request.user.patient.emergencyFirstName,
                                      'emergencyLastName': request.user.patient.emergencyLastName,
                                      'emergencyPhone': request.user.patient.emergencyPhone,
                                      # 'allergies': request.user.allergies,
                                      # 'recentOps': request.user.recentOps,
                                      # 'gender': request.user.gender,
                                      # 'prescriptions': request.user.prescriptions,
                                      })


# View to change information for the user.
# TODO: Make this a thing!
def account_info_change_view(request):
    return render_to_response('account_info_change.html')


# Allows user to log into the site
def auth_login(request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


# attempt to authorize the user, redirects to success or fail page as needed
def auth_view(request):
        username = 'username'
        password = 'password'
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

        '''
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            username = ''
        if 'password' in request.POST:
            password = request.POST['password']
        else:
            password = ''
        '''
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(request, user)
                        log_loggedIn = LogEntry(actor="System", entryType="Login", details=user.username + " logged in.")
                        log_loggedIn.save()
                        return HttpResponseRedirect('/loggedin')
        else:
                return HttpResponseRedirect('/invalid')

# homepage, visible only to those logged into the site.
@login_required(login_url='/login/')
def loggedin(request):
        return render_to_response('loggedin.html', {'username': request.user.username})


# Displays a page stating that the login attempt was invalid
def invalid_login(request):
        return render_to_response('invalid_login.html')


# Logs out the current user
def auth_logout(request):
        logout(request)
        return render_to_response('logout.html')


# Returns a successful register html page
def register_success(request):
        return render_to_response('register_success.html')


# Returns the register patient page
class RegisterPatientWizard(SessionWizardView):
        template_name = 'register.html'

        def done(self, form_list, **kwargs):
                form_data = [form.cleaned_data for form in form_list]
                user = User.objects.create_user(username=form_data[0]['username'],
                                                email=form_data[0]['email'],
                                                password=form_data[0]['password2'],
                                                first_name=form_data[0]['first_name'],
                                                last_name=form_data[0]['last_name'])
                patient = Patient.objects.create_patient(user=user,
                                                         phone=form_data[1]['phone'],
                                                         insuranceID=form_data[1]['insuranceID'],
                                                         sex=form_data[1]['sex'],
                                                         emergencyFirstName=form_data[2]['emergencyFirstName'],
                                                         emergencyLastName=form_data[2]['emergencyLastName'],
                                                         emergencyPhone=form_data[2]['emergencyPhone'])

                if form_data[1]['doctor'] != None:
                        patient.associated_doctor = form_data[1]['doctor']
                if form_data[1]['hospital'] != None:
                        patient.hospital = form_data[1]['hospital']
                if form_data[1]['dateOfBirth'] != None:
                        patient.dateOfBirth = form_data[1]['dateOfBirth']
                if form_data[1]['height'] != None:
                        patient.height = form_data[1]['height']
                if form_data[1]['weight'] != None:
                        patient.weight = form_data[1]['weight']
                user.save()
                patient.save()
                userN = form_data[0]['username']
                log_newUser = LogEntry(actor="System", entryType="Patient", details=userN + " created.")
                log_newUser.save()
                return HttpResponseRedirect('/register_success/')

class RegisterEmployeeWizard(SessionWizardView):
        template_name = 'register_emp.html'
        def done(self, form_list, **kwargs):
                form_data = [form.cleaned_data for form in form_list]
                user = User.objects.create_user(username=form_data[0]['username'],
                                                email=form_data[0]['email'],
                                                password=form_data[0]['password2'],
                                                first_name=form_data[0]['first_name'],
                                                last_name=form_data[0]['last_name'])
                userType=form_data[0]['userType']
                user.save()
                if userType == 'Nurse':
                        nurse = Nurse.objects.create_nurse(user=user,
                                                           hospital=form_data[0]['hospital'])
                        nurse.save()
                        log_newNurse = LogEntry(actor="System", entryType="New Nurse", details=user.username + " was created.")
                        log_newNurse.save()
                elif userType == 'Doctor':
                        doctor = Doctor.objects.create_doctor(user=user,
                                                              hospital=form_data[0]['hospital'])
                        doctor.save()
                        log_newDoctor = LogEntry(actor="System", entryType="New Doctor", details=user.username + " was created.")
                        log_newDoctor.save()
                else:
                        admin = Administrator.objects.create_admin(user=user,
                                                                   hospital=form_data[0]['hospital'])
                        log_newAdmin = LogEntry(actor="System", entryType="New Admin", details=user.username + " was created.")
                        log_newAdmin.save()
                return HttpResponseRedirect('/register_success/')
                                                
