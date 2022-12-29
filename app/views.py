from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is my first project')
def suresh(request):
    return HttpResponse('<h1><marquee>hi suresh have a good day</marquee></h1>')
def sami(request):
    return HttpResponse('<h1>hello sami</h1>')
def Regform(request):
    return HttpResponse('<h1>hellooollo sami</h1>')