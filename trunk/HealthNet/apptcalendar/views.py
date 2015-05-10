from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # will use redirects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apptcalendar.models import Day, Event, Month, CalendarHome
from apptcalendar.forms import apptRegistration
from SystemObjects.models import Appointment, Doctor, Patient, User, LogEntry
from django.core.context_processors import csrf
import datetime
import calendar
from django.contrib.formtools.wizard.views import SessionWizardView

# The following unused imports were removed in R1 Refactoring:
# django.shortcuts.render django.http.HttpResponseRedirect


def makeString(n, m=0):  # n = day_id
    s = str(n)  #m = m_id
    if s[0] == '-':  #negative n means the month is uninitialized
        s2 = str(m)
        s = s2[:] + '/' + s[1:]  #s[1:] is what day of the month it is
    return '/calendar/day/' + s[:];


def makeStringM(mid, current_month):  # mid=linked month_id
    s = str(mid)  #current_month=month_id linked from
    if s[:] == '-2':  #-2 means the month before user's first month
        s = 'none'
    elif s[:] == '-1':  #-1 means the soonest uninitialized month
        s = 'new/' + str(current_month.id)
    return '/calendar/month/' + s[:];


@login_required(login_url='/login/')
def viewNewMonth(request, current_month_id):
    current_month = get_object_or_404(Month, pk=current_month_id)
    if not current_month.nextmonth_id == -1:
        return HttpResponseRedirect("/calendar/month/" + \
                                    str(current_month.nextmonth_id))
    m = newMonth(current_month)
    return HttpResponseRedirect("/calendar/month/" + str(m.id))


@login_required(login_url='/login/')
def newMonth(current_month):
    firstday = current_month.startdate
    newmonth = firstday.month
    newyear = (firstday.year + newmonth // 12)
    newmonth = newmonth % 12 + 1
    newday = min(firstday.day, calendar.monthrange(newyear, newmonth)[1])
    newdate = datetime.date(newyear, newmonth, newday)
    m = Month(startdate=newdate, \
              user=current_month.user, \
              lastmonth_id=current_month.id)
    m.save()
    current_month.nextmonth_id = m.id
    current_month.save()
    return m


@login_required(login_url='/login/')
def noMonth(request):
    return HttpResponse("This month is both in the past and uninitialized.")


@login_required(login_url='/login/')
def viewMonth(request, month_id):
    thisuser = request.user
    mid = int(month_id)
    m = get_object_or_404(Month, pk=month_id)
    muser = m.user
    if not thisuser == muser:
        return HttpResponse("You cant see this page, " \
                            + thisuser.username)
    s = (thisuser.username + ': ')
    if (m.startdate.month == 1):
        s += "January "
    elif (m.startdate.month == 2):
        s += "February "
    elif (m.startdate.month == 3):
        s += "March "
    elif (m.startdate.month == 4):
        s += "April "
    elif (m.startdate.month == 5):
        s += "May "
    elif (m.startdate.month == 6):
        s += "June "
    elif (m.startdate.month == 7):
        s += "July "
    elif (m.startdate.month == 8):
        s += "August "
    elif (m.startdate.month == 9):
        s += "September "
    elif (m.startdate.month == 10):
        s += "October "
    elif (m.startdate.month == 11):
        s += "November "
    elif (m.startdate.month == 12):
        s += "December "
    s += str(m.startdate.year)
    s += ('<br><a href = "' + makeString(m.day1, m=m.id) + '/">Day1</a><br>' \
                                                           '<a href = "' + makeString(m.day2,
                                                                                      m=m.id) + '/">Day2</a><br>' \
                                                                                                '<a href = "' + makeString(
        m.day3, m=m.id) + '/">Day3</a><br>' \
                          '<a href = "' + makeString(m.day4, m=m.id) + '/">Day4</a><br>' \
                                                                       '<a href = "' + makeString(m.day5,
                                                                                                  m=m.id) + '/">Day5</a><br>' \
                                                                                                            '<a href = "' + makeString(
        m.day6, m=m.id) + '/">Day6</a><br>' \
                          '<a href = "' + makeString(m.day7, m=m.id) + '/">Day7</a><br>' \
                                                                       '<a href = "' + makeString(m.day8,
                                                                                                  m=m.id) + '/">Day8</a><br>' \
                                                                                                            '<a href = "' + makeString(
        m.day9, m=m.id) + '/">Day9</a><br>' \
                          '<a href = "' + makeString(m.day10, m=m.id) + '/">Day10</a><br>' \
                                                                        '<a href = "' + makeString(m.day11,
                                                                                                   m=m.id) + '/">Day11</a><br>' \
                                                                                                             '<a href = "' + makeString(
        m.day12, m=m.id) + '/">Day12</a><br>' \
                           '<a href = "' + makeString(m.day13, m=m.id) + '/">Day13</a><br>' \
                                                                         '<a href = "' + makeString(m.day14,
                                                                                                    m=m.id) + '/">Day14</a><br>' \
                                                                                                              '<a href = "' + makeString(
        m.day15, m=m.id) + '/">Day15</a><br>' \
                           '<a href = "' + makeString(m.day16, m=m.id) + '/">Day16</a><br>' \
                                                                         '<a href = "' + makeString(m.day17,
                                                                                                    m=m.id) + '/">Day17</a><br>' \
                                                                                                              '<a href = "' + makeString(
        m.day18, m=m.id) + '/">Day18</a><br>' \
                           '<a href = "' + makeString(m.day19, m=m.id) + '/">Day19</a><br>' \
                                                                         '<a href = "' + makeString(m.day20,
                                                                                                    m=m.id) + '/">Day20</a><br>' \
                                                                                                              '<a href = "' + makeString(
        m.day21, m=m.id) + '/">Day21</a><br>' \
                           '<a href = "' + makeString(m.day22, m=m.id) + '/">Day22</a><br>' \
                                                                         '<a href = "' + makeString(m.day23,
                                                                                                    m=m.id) + '/">Day23</a><br>' \
                                                                                                              '<a href = "' + makeString(
        m.day24, m=m.id) + '/">Day24</a><br>' \
                           '<a href = "' + makeString(m.day25, m=m.id) + '/">Day25</a><br>' \
                                                                         '<a href = "' + makeString(m.day26,
                                                                                                    m=m.id) + '/">Day26</a><br>' \
                                                                                                              '<a href = "' + makeString(
        m.day27, m=m.id) + '/">Day27</a><br>' \
                           '<a href = "' + makeString(m.day28, m=m.id) + '/">Day28</a><br>')
    dplus = datetime.timedelta(days=28)
    dfirst = m.startdate
    if not ((dfirst + dplus).day == 1):
        s += '<a href = "' + makeString(m.day29, m=m.id) + '/">Day29</a><br>'
        dplus += datetime.timedelta(days=1)
        if not ((dfirst + dplus).day == 1):
            s += '<a href = "' + makeString(m.day30, m=m.id) + '/">Day30</a><br>'
            dplus += datetime.timedelta(days=1)
            if not ((dfirst + dplus).day == 1):
                s += '<a href = "' + makeString(m.day31, m=m.id) + '/">Day31</a><br>'
                dplus += datetime.timedelta(days=1)
    s += ('<a href = "' + makeStringM(m.nextmonth_id, m) + '/">Next</a><br>')
    if not m.lastmonth_id == -2:
        s += ('<a href = "' + makeStringM(m.lastmonth_id, m) + '/">Last</a>')
    return HttpResponse(s)


@login_required(login_url='/login/')
def viewCalendar(request):
    thisuser = request.user
    try:
        c = CalendarHome.objects.get(user=thisuser)
    except CalendarHome.DoesNotExist:
        m = Month(user=thisuser)
        m.save()
        c = CalendarHome(user=thisuser, currentmonth=m)
        c.save()
    m = c.currentmonth
    while (m.startdate.month < datetime.date.today().month) \
            or (m.startdate.year < datetime.date.today().year):
        c.currentmonth = newMonth(m)
        m = c.currentmonth
    c.save()
    return HttpResponseRedirect("/calendar/month/" + str(m.id))


@login_required(login_url='/login/')
def newDay(request, dayofthemonth, month_id):
    thisuser = request.user
    m = get_object_or_404(Month, pk=month_id)
    n = int(dayofthemonth)
    if (not (m.day1 == 0 - n) \
                and not (m.day2 == 0 - n) \
                and not (m.day3 == 0 - n) \
                and not (m.day4 == 0 - n) \
                and not (m.day5 == 0 - n) \
                and not (m.day6 == 0 - n) \
                and not (m.day7 == 0 - n) \
                and not (m.day8 == 0 - n) \
                and not (m.day9 == 0 - n) \
                and not (m.day10 == 0 - n) \
                and not (m.day11 == 0 - n) \
                and not (m.day12 == 0 - n) \
                and not (m.day13 == 0 - n) \
                and not (m.day14 == 0 - n) \
                and not (m.day15 == 0 - n) \
                and not (m.day16 == 0 - n) \
                and not (m.day17 == 0 - n) \
                and not (m.day18 == 0 - n) \
                and not (m.day19 == 0 - n) \
                and not (m.day20 == 0 - n) \
                and not (m.day21 == 0 - n) \
                and not (m.day22 == 0 - n) \
                and not (m.day23 == 0 - n) \
                and not (m.day24 == 0 - n) \
                and not (m.day25 == 0 - n) \
                and not (m.day26 == 0 - n) \
                and not (m.day27 == 0 - n) \
                and not (m.day28 == 0 - n) \
                and not (m.day29 == 0 - n) \
                and not (m.day30 == 0 - n) \
                and not (m.day31 == 0 - n)):
        return HttpResponseRedirect("/calendar/month/" + str(month_id))
    d = Day(date=m.startdate.replace(day=n), \
            user=thisuser)
    d.save()
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
    return HttpResponseRedirect("/calendar/day/" + str(d.id))


# Displays the details of a single day
@login_required(login_url='/login/')
def viewDay(request, day_id):
    thisuser = request.user
    n = int(day_id)
    d = get_object_or_404(Day, pk=day_id)
    duser = d.user
    if not thisuser == duser:
        return HttpResponse("You cant see this page, " \
                            + thisuser.username)
    ddate = d.date
    s = (thisuser.username + ": ")

    weekdaynumber = d.date.weekday()
    if weekdaynumber == 0:
        s += "Monday, "
    elif weekdaynumber == 1:
        s += "Tuesday, "
    elif weekdaynumber == 2:
        s += "Wednesday, "
    elif weekdaynumber == 3:
        s += "Thursday, "
    elif weekdaynumber == 4:
        s += "Friday, "
    elif weekdaynumber == 5:
        s += "Saturday, "
    elif weekdaynumber == 6:
        s += "Sunday, "

    monthnumber = d.date.month
    if (monthnumber == 1):
        s += "January "
    elif (monthnumber == 2):
        s += "February "
    elif (monthnumber == 3):
        s += "March "
    elif (monthnumber == 4):
        s += "April "
    elif (monthnumber == 5):
        s += "May "
    elif (monthnumber == 6):
        s += "June "
    elif (monthnumber == 7):
        s += "July "
    elif (monthnumber == 8):
        s += "August "
    elif (monthnumber == 9):
        s += "September "
    elif (monthnumber == 10):
        s += "October "
    elif (monthnumber == 11):
        s += "November "
    elif (monthnumber == 12):
        s += "December "
    s += str(d.date.day)
    s += ", "
    s += str(d.date.year)
    return HttpResponse(s)


# Register a new Event on a given day
@login_required(login_url='/login/')
def newEvent(request, day_id):
    e = Event()
    e.day_id = day_id
    e.user = request.user
    e.sart = e.end = None
    e.name = ''
    e.start = request.POST.get('start', None)
    e.end = request.POST.get('end', None)
    e.name = request.POST.name('event name', '')
    e.save()
    return HttpResponse("New Event Page")


# Detail view of a single event
@login_required(login_url='/login/')
def viewEvent(request, event_id):
    thisuser = request.user
    e = get_object_or_404(Event, pk=event_id)
    dnumber = e.day_id
    d = get_object_or_404(Day, pk=dnumber)
    euser = d.user_id
    if thisuser != get_object_or_404(User, pk=euser):
        return HttpResponse("You cant see this page, " + thisuser.username)
    else:
        eventstring = "You are viewing event " + str(event_id) + "\n" + \
                      "This event starts at " + str(e.start) + " and ends at " + \
                      str(e.end) + "\n" + \
                      "Event name: " + e.name + "\n" + \
                      "Event day: " + str(e.day_id)
    return HttpResponse(eventstring)


# List all current appointments
@login_required(login_url='/login/')
def listAppts(request):
    fname = request.user.first_name
    lname = request.user.last_name
    return render_to_response('appt_list.html', {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'username': request.user.username,
        'apptsPatient': Appointment.objects.filter(Patient__first_name=fname, Patient__last_name=lname),
        'apptsDoctor': Appointment.objects.filter(Doctor__first_name=fname, Doctor__last_name=lname)
    })


# Detail view of a single appointment
@login_required(login_url='/login/')
def apptDetailView(request, appointment_id):
    return render_to_response('viewappt.html', {
        'id': appointment_id,
        'appt': Appointment.objects.get(pk=appointment_id)
    })


@login_required(login_url='/login/')
def register_appt(request):
    if request.method == 'POST':
        form = apptRegistration(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_appt_success')
    args = {}
    args.update(csrf(request))
    args['form'] = apptRegistration()
    return render_to_response('register_appt.html', args)


class registerPatientAppointmentWizard(SessionWizardView):
    template_name = 'register_appt.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        appt = Appointment.objects.create_appointment(patient=self.request.user.patient,
                                                     doctor=form_data[0]['doctor'],
                                                     time=form_data[0]['time'],)
        appt.save()
        log_patientAppt = LogEntry(actor="System", entryType="Patient", details="appointment created")
        log_patientAppt.save()
        return HttpResponseRedirect('new_appt_success')


class registerDoctorAppointmentWizard(SessionWizardView):
    template_name = 'register_appt.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        appt = Appointment.objects.create_appointment(doctor=self.request.user.doctor,
                                                      patient=form_data[0]['patient'],
                                                      time=form_data[0]['time'],)
        appt.save()
        log_patientAppt = LogEntry(actor="System", entryType="Patient", details="appointment created")
        log_patientAppt.save()
        return HttpResponseRedirect('new_appt_success')

@login_required(login_url='login')
def newApptSuccess(request):
    return render_to_response('new_appt_success.html')
