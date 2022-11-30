from django.http import request
from  django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def HOME(request):
    return render(request,'homePage.html')


def LOGIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'No user found')
            return redirect('registration')

    return render(request,'login.html')


def REGISTRATION(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username already taken')
            return redirect('registration')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already taken')
            return redirect('registration')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request,'User created successfully')
            return redirect('login')

    return render(request,'registration.html')


def LOGOUT(request):
    auth.logout(request)
    return redirect('login')