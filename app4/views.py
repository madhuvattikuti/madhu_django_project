from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def d1(request):
    return HttpResponse("hii this is d1 functionality")
def d2(request):
    return HttpResponse("hi this is d2 functionality")
def d3(request):
    return HttpResponse("hi this is d3 functionality")