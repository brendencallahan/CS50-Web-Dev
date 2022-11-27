from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "wiki/index.html")

def greet(request, name):
    return render(request, "wiki/greet.html", {
        "name": name.capitalize()
    })