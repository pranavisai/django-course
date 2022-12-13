from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('hello from Pranavi.')


def calculate():
    x=1
    y=2
    return x+y

def say_html(request):
    x = calculate()
    return render(request, 'hello.html', {'names': 'Your Highness'})