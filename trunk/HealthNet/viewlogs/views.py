from django.shortcuts import render, get_object_or_404
from SystemObjects.models import LogEntry
from django.http import HttpResponse, HttpResponseRedirect
import datetime


# require admin permission here
def viewRecent(request):
    # TODO: Make this HTML Work
    entryCount=5  # This may be useful to allow you to change the number of visible logs
    logs = LogEntry.objects.order_by('-id')[:entryCount]
    s = ("Most recent %d log entries:" % entryCount)
    for o in logs:
        s += " " + str(o)
    return HttpResponse(s)


# require admin permission here
def viewLog(request, log_id):
    # TODO: Replace HttpResponse
    o = get_object_or_404(LogEntry, pk=log_id)
    time = o.time  #datetimefield
    actor = o.actor  #string
    entrytype = o.entryType  #string
    details = o.details  #string
    # makehtml
    return HttpResponse("You are viewing log # " + str(log_id))