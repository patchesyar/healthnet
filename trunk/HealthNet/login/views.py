from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.db import models
from django.views import generic
#from login.models import 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from login.forms import HealthNetRegistration
from django.contrib.auth.decorators import login_required

def auth_login(request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)

        
def auth_view(request):
        username = password = ''
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
        if (not user == None):
                if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/loggedin')
        else:
                return HttpResponseRedirect('/invalid')

@login_required(login_url='/login/')
def loggedin(request):
        return render_to_response('loggedin.html', {'username': request.user.username})

def invalid_login(request):
        return render_to_response('invalid_login.html')

def auth_logout(request):
        logout(request)
        return render_to_response('logout.html')

def register_user(request):
        if request.method == 'POST':
                form = HealthNetRegistration(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/register_success')
        args = {}
        args.update(csrf(request))
        args['form'] = HealthNetRegistration()
        return render_to_response('register.html', args)

def register_success(request):
        return render_to_response('register_success.html')
