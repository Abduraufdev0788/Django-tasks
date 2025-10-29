from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(a):
    return HttpResponse("Bosh sahifa")

def about(a):
    return HttpResponse("haqida")
def contact(a):
    return HttpResponse("Contcts")

def login(a):
    return HttpResponse("login")

def register(a):
    return HttpResponse("registratsiya")

def profile(a):
    return HttpResponse("Bosh profile")
