from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check is the user loging in
    if request.method=='POST':
        username=request.POST['User_name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successfull")
            return redirect('home')
        else:
           messages.success(request,"Error...")
           return redirect('home')
    else:
        return render(request,'home.html',{})

def User_logout(request):
     logout(request)
     messages.success(request,"You have been logout")
     return redirect('home')

def User_register(request):
  return render(request,'register.html',{})