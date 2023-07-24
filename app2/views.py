from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_first(request):
    return HttpResponse('<marquee><h1>App2 first response</h1></marquee>')

def app2_second(request):
    return HttpResponse('<marquee><h1>App2 second reponse</h2></marquee>')

