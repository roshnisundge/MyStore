from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def info(r):
    return HttpResponse('<h1> Welcome to MyApp Store </h1>')