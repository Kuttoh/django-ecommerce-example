from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()

    return render(request, 'hello.html', {
        'name':'Isaac', 
        'message' : 'Continue learning!'
        })
