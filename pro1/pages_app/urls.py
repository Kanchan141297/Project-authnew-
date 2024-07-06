from django.urls import path,re_path
from .views import *

urlpatterns =[
    path("",HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    re_path("^.*$",ErrorView.as_view(),name="error")
]