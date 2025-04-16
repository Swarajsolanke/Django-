from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hi")

def index(request):
    return HttpResponse("hello")

def learn(request):
    return HttpResponse("<h1>hey there</h1>")





