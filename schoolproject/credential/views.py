from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def demo(request):
    return render(request,"Home.html")
def Login(request):
     if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login(request,user)
            return redirect("/credential/catalog")
         else:
            messages.info(request,'Invalid credential')
            return redirect("/credential")
     return render(request,"Login.html")

def register(request):
      if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
          if User.objects.filter(username=username).exists():
             messages.info(request,"Username taken")
             return  redirect('/credential/register')
          else:
            user=User.objects.create_user(username=username,password=password)
            user.save();
            messages.success(request,"Your account has been created")
            return redirect("/credential/Login")
        else:
          messages.info(request,"Password not matching")
     #    return redirect('register')
     #      return redirect('/credential')
      return render(request,"register.html")
# Create your views here.
def catalog(request):
    return render(request,'catalog.html')
def regform(request):
    return render(request, 'regform.html')
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/credential')