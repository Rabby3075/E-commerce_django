from django.http import request
from  django.shortcuts import render


def HOME(request):
    return render(request,'homePage.html')


def LOGIN(request):
    return render(request,'login.html')


def REGISTRATION(request):
    return render(request,'registration.html')