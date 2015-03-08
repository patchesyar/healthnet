from django.shortcuts import render
from django.http import *
from django.views import generic
from SystemObjects.models import Appointment


# Create your views here.
#class ApptListView(generic.ListView):
#    template_name = 'listview.html'
#    context_object_name = 'appointment_list'

#    def get_queryset(self):
#        return Appointment.objects.filter.order_by('time')

def test(request):
    return HttpResponse("testttt")

#def index(request):
#    return HttpResponse("this is a system objects view i think.")

#def index2(request):
#    return HttpResponse("Looks like you've managed to find index2")

#def detail(request, obj_id):
#    return HttpResponse("You're looking at object %s." % obj_id)
