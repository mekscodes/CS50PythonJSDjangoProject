from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world 1!")

def brian(request):
    return HttpResponse("Hello, Brian!")  
    
age=2037-1987
def greet(request,name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize(),
    })

def index(request):
    return render(request,"hello/index.html")
