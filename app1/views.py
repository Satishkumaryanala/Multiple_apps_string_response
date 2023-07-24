from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_first(request):
    return HttpResponse('<marquee><h1>App1 first response</h1></marquee>')

def app1_second(request):
    return HttpResponse('<marquee><h1>App1 second reponse</h1></marquee>')
