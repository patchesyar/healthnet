from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from messaging.models import Message
import datetime

@login_required(login_url='/login/')
def redirectToInbox(request):
	return HttpResponseRedirect('inbox/1/')

@login_required(login_url='/login/')
def viewMessage(request, message_id):
	thisuser = request.user
	message = get_object_or_404(Message, pk=message_id)
	sentby = message.sentby
	sentto = message.sentto
	if (not thisuser == sentby) and (not thisuser == sentto):
		return HttpResponse("You can't view this page, " +\
				thisuser.username)
	context = {'message': message}
	return render(request, 'viewmessage.html', context)

@login_required(login_url='/login/')
def viewInbox(request, page):
	pageint = int(page)
	start = pageint - 1
	notfirst = False
	notlast = False
	if not pageint == 1:
		notfirst = True
	start = start * 10#the location of the first message being got
	thisuser = request.user
	messages = (Message.objects.filter(sentto=thisuser)\
			).order_by('-timesent')
	if len(messages) > start+9:
		recent_messages = messages[start:(start+9)]
		notlast = True
	elif len(messages) > start:
		recent_messages = messages[start:]
	else:
		recent_messages = []
	lastpage = pageint-1
	nextpage = pageint+1
	context = {'recent_messages': recent_messages, 'notfirst': notfirst,\
			'notlast': notlast, 'lastpage': lastpage,\
			'nextpage': nextpage}
	return render(request, 'inbox.html', context)

@login_required(login_url='/login/')
def viewOutbox(request, page):
	pageint = int(page)
	start = pageint - 1
	notfirst = False
	notlast = False
	if not pageint == 1:
		notfirst = True
	start = start * 10#the location of the first message being got
	thisuser = request.user
	messages = (Message.objects.filter(sentby=thisuser)\
			).order_by('-timesent')
	if len(messages) > start+9:
		recent_messages = messages[start:(start+9)]
		notlast = True
	elif len(messages) > start:
		recent_messages = messages[start:]
	else:
		recent_messages = []
	lastpage = pageint-1
	nextpage = pageint+1
	context = {'recent_messages': recent_messages, 'notfirst': notfirst,\
			'notlast': notlast, 'lastpage': lastpage,\
			'nextpage': nextpage}
	return render(request, 'outbox.html', context)


@login_required(login_url='/login/')
def displayNewMessage(request):
	subject = ''
	c = {'subject': subject}
	c.update(csrf(request))
	return render_to_response('newmessage.html', c)

@login_required(login_url='/login/')
def newMessage(request):
	sendto = 'sendto'
	subject = 'subject'
	message = 'message'
	if request.POST:
		sendto = request.POST.get('sendto', '')
		subject = request.POST.get('subject', '')
		message = request.POST.get('message', '')
	sendbyuser = request.user
	sendtouser = get_object_or_404(User, username=sendto)
	now = datetime.datetime.now()
	m = Message(sentby=sendbyuser, sentto=sendtouser, timesent=now,\
			subject=subject, message=message)
	m.save()
	return HttpResponseRedirect('/messaging/outbox/1/')

























