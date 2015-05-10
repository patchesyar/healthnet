from django.conf.urls import patterns, url

from messaging import views

urlpatterns = patterns('',
		url(r'^$',\
				views.redirectToInbox, name = 'default url'),
		url(r'^view/(?P<message_id>\d+)/$',\
				views.viewMessage, name = 'view message'),
		url(r'^inbox/(?P<page>\d+)/$',\
				views.viewInbox, name = 'view inbox'),
		url(r'^outbox/(?P<page>\d+)/$',\
				views.viewOutbox, name = 'view outbox'),
		url(r'^new/$',\
				views.displayNewMessage, name = 'new message'),
		url(r'^new/send/$',\
				views.newMessage, name = 'send message')
)
