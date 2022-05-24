import email
import imp
from unittest.mock import patch
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from core.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def user_Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        messages.info(request,"Login Failed. Please Try Again!")
    #return render(request, 'accounts/index.html')
    return render(request, 'accounts/login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone_field')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists!")
                return redirect('user_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email already Exists!")
                    return redirect('user_register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    data = Customer(user=user, phone_field=phone)
                    data.save()
                    # code for Login of user will come here
                    our_user = authenticate(username=username, password=password)
                    if our_user is not None:
                        login(request, user)
                        return redirect('/')
        else:
            messages.info(request,"Password and Confirm Password Mismatch!")
            return redirect('user_register')
    return render(request, 'accounts/register.html')


def user_Logout(request):
   logout(request)
   return redirect('/')