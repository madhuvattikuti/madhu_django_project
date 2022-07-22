from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def e1(request):
    return HttpResponse("hii this is e1 functionality")
def e2(request):
    return HttpResponse("hi this is e2 functionality")
def e3(request):
    return HttpResponse("hi this is e3 functionality")