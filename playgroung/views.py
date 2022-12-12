from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    #pull data from db
    #transform
    #send emails
    return HttpResponse('Hello from Pranavi.')