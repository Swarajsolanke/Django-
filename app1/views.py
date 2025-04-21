from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hi")

def index(request):
    return HttpResponse("hello")

def learn(request,**kwargs):
    status=kwargs.get("status")
    print(f"this is the value of key argument: {status}")
    return HttpResponse(f"<h1>hey there {status}</h1>")
def study(req, **kwargs):
    status=kwargs.get('status',"not allowed")
    print(f"this is the study matreial end point:{status}")
    return HttpResponse(f"wow you made it:{status}")






