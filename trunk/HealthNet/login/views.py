from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from login.forms import HealthNetRegistration
from django.contrib.auth.decorators import login_required

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
                                      # 'dob': request.user.dob,
                                      # 'phone': request.user.phone,
                                      # 'ID': request.user.ID,
                                      'username': request.user.username,
                                      # 'prefHos': request.user.prefHos,
                                      # 'efirstName': request.user.efirstName,
                                      # 'elastName': request.user.elastName,
                                      # 'ePhone': request.user.ePhone,
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


# Shows the registration page to the user to input their information
def register_user(request):
        if request.method == 'POST':
                form = HealthNetRegistration(request.POST)
                print(form.is_valid())
                print(form.errors)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/register_success')
        args = {}
        args.update(csrf(request))
        args['form'] = HealthNetRegistration()
        return render_to_response('register.html', args)


# Returns a successful register html page
def register_success(request):
        return render_to_response('register_success.html')

# Returns the register patient page
def reg_p(request):
        return render_to_response('reg_p.html')

# Returns the register doctor page
def reg_d(request):
        return render_to_response('reg_d.html')

# Returns the register nurse page
def reg_n(request):
        return render_to_response('reg_n.html')

# Returns the register admin page
def reg_a(request):
        return render_to_response('reg_a.html')
