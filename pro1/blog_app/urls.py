from django.urls import path

from .views import *

urlpatterns =[
    path("add/",AddView.as_view(),name="add"),
    path("show/",ShowView.as_view(),name="show"),
    path("update/<int:pk>/",UpdateView.as_view(),name="update"),
    path("delete/<int:pk>/",DeleteView.as_view(),name="delete"),
    path("see/<int:pk>/",SeeView.as_view(),name="see")

]