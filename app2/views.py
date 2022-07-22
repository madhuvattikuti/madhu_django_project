from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def b1(request):
    return HttpResponse("hii this is b1 functionality")
def b2(request):
    return HttpResponse("hi this is b2 functionality")
def b3(request):
    return HttpResponse("hi this is b3 functionality")