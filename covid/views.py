import requests
from django.shortcuts import render
from . import models

def home(request):
	return render(request, 'base.html')

def chose_state(request):
	state = request.POST.get('state')
	models.State.objects.create(state=state)

	stuff_for_frontend = {
	'state': state,
	}
	return render(request, 'covid/chose_state.html', stuff_for_frontend)

def tips(request):
	return render(request, 'covid/tips.html')

def info(request):
	return render(request, 'covid/info.html')

def fake(request):
	return render(request, 'covid/fake.html')