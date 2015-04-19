from django.conf.urls import patterns, url

from apptcalendar import views

urlpatterns = patterns('',
                       url(r'^$', views.viewCalendar, name='calendar'),
                       url(r'^day/(?P<day_id>\d+)/$', views.viewDay, name='day'),
                       url(r'^day/(?P<month_id>\d+)/(?P<dayofthemonth>\d+)/$',
                           views.newDay, name='newday'),
                       url(r'^event/(?P<event_id>\d+)/$', views.viewEvent, name='event'),
                       url(r'^appointment/$', views.listAppts, name='viewappt'),
                       url(r'^appointment/(?P<appointment_id>\d+)/$',
                           views.apptDetailView, name='appt'),
                       url(r'^month/none/$', views.noMonth, name='nomonth'),
                       url(r'^month/new/(?P<current_month_id>\d+)/$',
                           views.viewNewMonth, name='newmonth'),
                       url(r'^month/(?P<month_id>\d+)/$', views.viewMonth, name='viewmonth'),
                       url(r'^appointment/new/$', views.register_appt, name="newappt"),
                       url(r'^appointment/new/success/', views.newApptSuccess, name="newapptsuccess"),
                       )
