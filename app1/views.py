from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_first(request):
    return HttpResponse("This is the first function of app1")
def app1_second(request):
    return HttpResponse("This is the second function of app1")