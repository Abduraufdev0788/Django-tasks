from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



def home(requests:HttpRequest):
  return render(request=requests, template_name='home.html')

def bosh_sahifa(requests:HttpRequest):
  return render(request=requests, template_name="index.html")

def books(requests:HttpRequest):
  return render(request=requests, template_name="books.html")
def register(requests:HttpRequest):
  return render(request=requests, template_name="register.html")
def aloqa(requests:HttpRequest):
  return render(request=requests, template_name="contact.html")