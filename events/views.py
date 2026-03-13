from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def event_list(request):
	return HttpResponse("Event list test")