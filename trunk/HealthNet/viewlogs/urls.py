from django.conf.urls import patterns, url

from viewlogs import views

urlpatterns = patterns('',
                       url(r'^$', views.viewRecent, name='mainpage'),  # Main page for viewing logs
                       url(r'^id/(?P<log_id>\d+)/$', views.viewLog, name='detail')  # Detail view of one LogEntry
)
