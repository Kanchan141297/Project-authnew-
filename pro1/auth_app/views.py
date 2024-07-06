from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login,logout
from django.http import HttpResponse
# Create your views here.

class SignupView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,"auth_app/signup.html",{"form":form})
    def post(self,request):
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request,"auth_app/signup.html",{"form":form})

class LoginView(View):
    def get(self,request):
        return render(request,"auth_app/login.html",{})
    def post(self,request):
        u = request.POST.get("nm")
        p = request.POST.get("pwd")
        user = authenticate(username = u,password = p)
        if user:
            login(request,user)
            return redirect("add")
        return render(request,"auth_app/login.html",{})
