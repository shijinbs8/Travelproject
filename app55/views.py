from email import message

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method=='POST':
        username2=request.POST["username"]
        password2=request.POST["password"]
        user=auth.authenticate(username=username2,password=password2)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method== 'POST':
        username1=request.POST["User_name"]
        firstname1=request.POST["first_name"]
        lastname1=request.POST["last_name"]
        email1=request.POST["email"]
        password1=request.POST['password']
        cpassword=request.POST['cpassword']
        if password1==cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request,"EMAIL ALREADY TAKEN")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username1,first_name=firstname1,last_name=lastname1,email=email1,
                                              password=password1)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')