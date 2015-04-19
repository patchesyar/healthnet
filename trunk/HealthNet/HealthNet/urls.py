from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HealthNet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^account/','login.views.account_view'),
    url(r'^account_info_change/','login.views.account_info_change_view'),
    url(r'^under_construction/', 'apptcalendar.views.viewCalendar'),
    url(r'^login/$', 'login.views.auth_login'),
    url(r'^auth/$', 'login.views.auth_view'),
    url(r'^logout/$', 'login.views.auth_logout'),
    url(r'^loggedin/$', 'login.views.loggedin'),
    url(r'^invalid/$', 'login.views.invalid_login'),
    url(r'^register/$', 'login.views.register_user'),
    url(r'^register_success/$', 'login.views.register_success'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'HealthNet.views.home'),
    url(r'^calendar/', include('apptcalendar.urls')),
    url(r'^logs/', include('viewlogs.urls')),
    url(r'^information/', include('userinformation.urls')),
    url(r'^header/', 'HealthNet.views.header'),
    url(r'^CSV/$', 'CSVFileApp.views.creation'),
    url(r'^CSVprocessing/$','CSVFileApp.views.processing'),
    url(r'^register/doctor/$', 'login.views.reg_d'),
    url(r'^register/nurse/$', 'login.views.reg_n'),
    url(r'^register/patient/$', 'login.views.reg_p'),
    url(r'^register/admin/$', 'login.views.reg_a'),
    url(r'^prescriptions/$','PrescriptionPage.views.main_page'),
    url(r'^prescription_stock/$','PrescriptionPage.views.stock'),
)
