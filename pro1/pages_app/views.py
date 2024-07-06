from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self,request):
        return  render(request,"pages_app/home.html",{})


class AboutView(View):
    def get(self, request):
        return render(request, "pages_app/about.html", {})

class ErrorView(View):
    def get(self, request):
        return render(request, "pages_app/error.html", {})
