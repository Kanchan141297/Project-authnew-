from django.shortcuts import render,redirect
from .forms import *
from .models import  *
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AddView(LoginRequiredMixin,View):
    login_url = "login"
    def get(self,request):
        form = BlogForm()
        return render(request,"blog_app/blog_form.html",{"form":form})
    def post(self,request):
        form =BlogForm(request.POST)
        if form.is_valid():
            b = form.save(commit=False)
            b.author = request.user
            b.save()
            return redirect("show")
        return render(request,"blog_app/blog_form.html",{"form":form})
class ShowView(LoginRequiredMixin,View):
    login_url = "login"
    def get(self,request):
        obj = Blog.objects.all()
        if request.GET:
            search = request.GET.get("search")
            obj = obj.filter(Q(title__contains= search)| Q(content__contains=search))
        return render(request,"blog_app/blog_list.html",{"obj":obj})

class UpdateView(LoginRequiredMixin,View):
    login_url = "login"
    def get(self, request,pk):
        obj= Blog.objects.get(id=pk)
        form = BlogForm(instance=obj)
        return render(request, "blog_app/update_blog.html", {"form":form})


    def post(self, request,pk):
        obj = Blog.objects.get(id=pk)
        form = BlogForm(request.POST,instance=obj)
        if form.is_valid():
            b = form.save(commit=False)
            b.author = request.user
            b.save()
            return redirect("show")
        return render(request, "blog_app/update_blog.html", {"form":form})

class DeleteView(LoginRequiredMixin,DeleteView):
    login_url = "login"
    model = Blog
    success_url = reverse_lazy("show")


class SeeView(LoginRequiredMixin,View):
    login_url = "login"
    def get(self, request,pk):
        obj= Blog.objects.get(id=pk)

        return render(request, "blog_app/seemore.html", {"obj":obj})


