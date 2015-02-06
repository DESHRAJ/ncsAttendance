from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime,timedelta

from ncs.models import ncsMembers

import random,string

def home(request):
	""" View for the home page"""
	if request.user.is_superuser:
		return render_to_response('index.html',context_instance=RequestContext(request))
	return HttpResponse("You are not logged in as SuperUser. <a href='/admin'>Click here </a> for logging in. ")
def attendance(request):
	""" View for the attendance marking """
	if request.POST:
		attendList = request.POST.getlist('list')
		total = userDetails.obejcts.all()
		j = 0
		for i in attendList:
			count = userDetails.objects.get()	 
	return render_to_response('attendance.html')

def addUser(request):
	""" View for adding a new user to the database """
	if request.user.is_superuser:
		print "$$$$$$$$$$$$$$$$$$$$$", request.path
		if request.POST:
			name  = request.POST['name']
			club = request.POST['club']
			print name
			print club
			ncsMembers.objects.create(name = name, club = club).save()
		return render_to_response('addUser.html',context_instance=RequestContext(request))
	return redirect('/admin/?next=/add')

# def stats(request):
# 	""" for showing the tats of every student who is attending the lab as same on github"""
# 	return render_to_response('stats.html', context_instance = RequestContext(request))

# def profile(request):
# 	"""" To show the individual profile of every nibble member """
# 	return render_to_response('profile.html')