from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('hello from Pranavi.')

def say_html(request):
    return render(request, 'hello.html')