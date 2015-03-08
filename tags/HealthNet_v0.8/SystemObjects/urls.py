from django.conf.urls import patterns, url

from SystemObjects import views

urlpatterns = patterns('',
    #most of these are wrong, just saying..
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index2, name='index2'),
    url(r'^(?O<obj_id>\d+)/$', views.detail, name='detail'),
)
