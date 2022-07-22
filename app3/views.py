from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def c1(request):
    return HttpResponse("hii this is c1 functionality")
def c2(request):
    return HttpResponse("hi this is c2 functionality")
def c3(request):
    return HttpResponse("hi this is c3 functionality")