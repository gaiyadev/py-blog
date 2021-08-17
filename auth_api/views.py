from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def signUp(request):
    return HttpResponse("sign up")


def signIn(request):
    return HttpResponse("sign In")
