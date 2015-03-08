from django.shortcuts import render, get_object_or_404
from SystemObjects.models import LogEntry
from django.http import HttpResponse, HttpResponseRedirect
import datetime

#require admin permission here
def viewRecent(request):
	#html gods pl0x please make this an actual thing
	logs = LogEntry.objects.order_by('-id')[:5]
	s = "Recent 5:"
	for o in logs:
		s += " "
		s += str(o)
	return HttpResponse(s)

#require admin permission here
def viewLog(request, log_id):
	o = get_object_or_404(LogEntry, pk=log_id)
	time = o.time#datetimefield
	actor = o.actor#string
	entrytype = o.entryType#string
	details = o.details#string
	#makehtml
	return HttpResponse("Kid you are viewing log # " + str(log_id))
