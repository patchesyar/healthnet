from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apptcalendar.models import Day, Event, Month
from SystemObjects.models import Appointment, Doctor, Patient, User
import datetime

def makeString(n):
	s = str(n)
	if s[0] == '-':
		s = 'new/' + s[1:]
	return '/calendar/day/' + s[:];

@login_required(login_url='/login/')
def viewCalendar(request):
	m = get_object_or_404(Month, pk=1)
	kid = request.user.username
	return HttpResponse("Hi " + kid +',\n'\
			"1: " + makeString(m.day1) + '\n'\
			"2: " + makeString(m.day2) + '\n'\
			"3: " + makeString(m.day3) + '\n'\
			"4: " + makeString(m.day4) + '\n'\
			"5: " + makeString(m.day5) + '\n'\
			"6: " + makeString(m.day6) + '\n'\
			"7: " + makeString(m.day7) + '\n'\
			"8: " + makeString(m.day8) + '\n'\
			"9: " + makeString(m.day9) + '\n'\
			"10: " + makeString(m.day10) + '\n'\
			"11: " + makeString(m.day11) + '\n'\
			"12: " + makeString(m.day12) + '\n'\
			"13: " + makeString(m.day13) + '\n'\
			"14: " + makeString(m.day14) + '\n'\
			"15: " + makeString(m.day15) + '\n'\
			"16: " + makeString(m.day16) + '\n'\
			"17: " + makeString(m.day17) + '\n'\
			"18: " + makeString(m.day18) + '\n'\
			"19: " + makeString(m.day19) + '\n'\
			"20: " + makeString(m.day20) + '\n'\
			"21: " + makeString(m.day21) + '\n'\
			"22: " + makeString(m.day22) + '\n'\
			"23: " + makeString(m.day23) + '\n'\
			"24: " + makeString(m.day24) + '\n'\
			"25: " + makeString(m.day25) + '\n'\
			"26: " + makeString(m.day26) + '\n'\
			"27: " + makeString(m.day27) + '\n'\
			"28: " + makeString(m.day28) + '\n'\
			"29: " + makeString(m.day29) + '\n'\
			"30: " + makeString(m.day30) + '\n'\
			"31: " + makeString(m.day31))

@login_required(login_url='/login/')
def newDay(request, dayofthemonth):
	thisuser = request.user
	n = int(dayofthemonth)
	d = Day(date = (datetime.date.today().replace(day=1) +\
			datetime.timedelta(days=n)), user = thisuser)
	d.save()
	m = get_object_or_404(Month, pk=1)
	if n == 1:
		m.day1 = d.id
	elif n == 2:
		m.day2 = d.id
	elif n == 3:
		m.day3 = d.id
	elif n == 4:
		m.day4 = d.id
	elif n == 5:
		m.day5 = d.id
	elif n == 6:
		m.day6 = d.id
	elif n == 7:
		m.day7 = d.id
	elif n == 8:
		m.day8 = d.id
	elif n == 9:
		m.day9 = d.id
	elif n == 10:
		m.day10 = d.id
	elif n == 11:
		m.day11 = d.id
	elif n == 12:
		m.day12 = d.id
	elif n == 13:
		m.day13 = d.id
	elif n == 14:
		m.day14 = d.id
	elif n == 15:
		m.day15 = d.id
	elif n == 16:
		m.day16 = d.id
	elif n == 17:
		m.day17 = d.id
	elif n == 18:
		m.day18 = d.id
	elif n == 19:
		m.day19 = d.id
	elif n == 20:
		m.day20 = d.id
	elif n == 21:
		m.day21 = d.id
	elif n == 22:
		m.day22 = d.id
	elif n == 23:
		m.day23 = d.id
	elif n == 24:
		m.day24 = d.id
	elif n == 25:
		m.day25 = d.id
	elif n == 26:
		m.day26 = d.id
	elif n == 27:
		m.day27 = d.id
	elif n == 28:
		m.day28 = d.id
	elif n == 29:
		m.day29 = d.id
	elif n == 30:
		m.day30 = d.id
	elif n == 31:
		m.day31 = d.id
	m.save()
	return viewDay(request, d.id) #should replace this with a redirect

@login_required(login_url='/login/')
def viewDay(request, day_id):
	thisuser = request.user
	n = int(day_id)
	d = get_object_or_404(Day, pk=day_id)
	duser = d.user_id
	if not thisuser == get_object_or_404(User, pk=duser):
		return HttpResponse("You cant see this page, "\
				+ thisuser.username)
	return HttpResponse("You are viewing day %s." % d.id)

@login_required(login_url='/login/')
def newEvent(request, day_id):
	e = Event()
	e.day_id = day_id
	e.user = request.user
	e.start = e.end = None
	e.name = ''
	e.start = request.POST.get('start', None)
	e.end = request.POST.get('end', None)
	e.name = request.POST.name('event name', '')
	e.save()
	return HttpResponse("New Event Page")

@login_required(login_url='/login/')
def viewEvent(request, event_id):
	thisuser = request.user
	e = get_object_or_404(Event, pk=event_id)
	dnumber = e.day_id
	d = get_object_or_404(Day, pk=dnumber)
	euser = d.user_id
	if not thisuser == get_object_or_404(User, pk=euser):
		return HttpResponse("You cant see this page, "\
				+ thisuser.username)
	eventstring = "You are viewing event " + str(event_id) +"\n" +\
		"This event starts at " + str(e.start) + " and ends at " +\
		str(e.end) + "\n" +\
		"Event name: " + e.name + "\n" +\
		"Event day: " + str(e.day_id)
	return HttpResponse(eventstring)

@login_required(login_url='/login/')
def listAppts(request):
	thisuser= request.user
	doctorAppointments= Appointment.objects.all()\
    #                        .get(Doctor__iexact==thisuser.username)
	return HttpResponse(doctorAppointments)

def viewAppt(request, Appointment_id):
	thisuser = request.user
	n = int(day_id)
	d = get_object_or_404(Day, pk=day_id)
	duser = d.user_id
	if not thisuser == get_object_or_404(User, pk=duser):
		return HttpResponse("You cant see this page, "\
				+ thisuser.username)
	return HttpResponse("You are viewing day %s." % d.id)