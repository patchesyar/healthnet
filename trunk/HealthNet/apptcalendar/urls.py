from django.conf.urls import patterns, url

from apptcalendar import views

urlpatterns = patterns('',
		url(r'^$', views.viewCalendar, name = 'calendar'),
		url(r'^day/(?P<day_id>\d+)/$', views.viewDay, name = 'day'),
		url(r'^day/new/(?P<dayofthemonth>\d+)/$', views.newDay, \
				name = 'newday'),
		url(r'^event/(?P<event_id>\d+)/$', views.viewEvent,\
				name = 'event'),
		url(r'^appointment/$', views.listAppts, name='viewappt')
		#url(r'^appointment/(?P<appointment_id>\d+)/$', views.viewAppt, name='appt')
)
