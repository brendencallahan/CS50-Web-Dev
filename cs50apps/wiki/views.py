from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def name(request):
    return HttpResponse("name")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")