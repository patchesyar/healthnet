from django.conf.urls import patterns, url

from userinformation import views

urlpatterns = patterns('',
                       url(r'^$', views.main_page, name='main page')  # Main page for viewing user info
)
