from django.conf.urls import patterns, url
# from django.conf.urls.default import *

# from login import views
from login.views import processing
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^login/$', 'login.views.processing'),
                       )
