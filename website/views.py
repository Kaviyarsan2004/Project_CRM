from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import record

def home(request):
    # Check is the user loging in
    records=record.objects.all()
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
        return render(request,'home.html',{'records':records})

def User_logout(request):
     logout(request)
     messages.success(request,"You have been logout")
     return redirect('home')

def User_register(request):
    if request.method=='POST':
      form=SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        #authenticate and login
        username =form.cleaned_data['username']
        password1=form.cleaned_data['password1']
        user=authenticate(username=username,password=password1)
        login(request,user)
        messages.success(request,'Successfully Registered!!')
        return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def User_record(request,pk):
    if request.user.is_authenticated:
        #lets look the records
        customer_record=record.objects.get(id=pk)
        return render(request,'records.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You need to Login first")
        return render(request,'home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        #lets delete the record
        delete_it=record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"The Record as been successfully deleted")
        return redirect('home')    
    else:
        messages.success(request,"Log in first")
        return render(request,'home')
    

def add_record(request):
     
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,'Record added Successfully')
                return redirect('home')
        return render(request,'add_record.html',{'form':form})

    else:
         messages.success(request,"Log in first")
         return render(request,'home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'record Updated..')
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
         messages.success(request,"Log in first")
         return render(request,'home')

        


