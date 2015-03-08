from django.conf.urls import patterns, url

from viewlogs import views

urlpatterns = patterns('',
		url(r'^$', views.viewRecent, name = 'mainpage'),
		url(r'^id/(?P<log_id>\d+)/$', views.viewLog, name = 'detail')
)
