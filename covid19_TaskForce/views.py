from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import pandas as pd


# Create your views here.
def index(request):    
    return render(request, 'index.html')

def output(request):
    total = (request.GET['total'])
    startdate = (request.GET['startdate'])
    noofquarantine = (request.GET['noofquarantine'])
    nonq = (request.GET['nonq'])
    room = (request.GET['room'])
    qt = (request.GET['qt'])

    print(total,startdate,noofquarantine,nonq)

    return render(request, 'output.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username= request.POST['username']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials!")    
            return redirect('login')


    else:    
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username= request.POST['username']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,"username taken!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email alredy taken")
                messages.info(request,"email already taken!")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                messages.info(request,"user created")
                return redirect('login')
        else:
            print("passwords do not macth!!")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
