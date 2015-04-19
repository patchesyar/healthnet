from django.shortcuts import *
from django.http import *

# Create your views here.


def home(request):
    return render(request, 'Home.html')


def testView(request):
    return render(request, 'testView.html')


def account_view(request):
    return render_to_response('account.html',{'username':request.user.username})

def header(request):
    return render(request, 'header.html')
