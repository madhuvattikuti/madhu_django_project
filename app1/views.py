from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a1(request):
    return HttpResponse("Hi this is a1 functionality")
def a2(request):
    return HttpResponse("hi this is a2 functionality")
def a3(request):
    return HttpResponse("hi this is a3 functionality")