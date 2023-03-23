from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.mvhome , name="MV Home"),
    path('/blizlalo' , views.blizlalo ,name="Bliz Lalo")
]
