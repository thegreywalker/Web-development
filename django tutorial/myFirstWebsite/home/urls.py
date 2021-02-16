from django.contrib import admin
from django.urls import path 
from home import views


urlpatterns = [
    path("",views.index, name="home"),
    path("home",views.index, name="home"),
    path("about",views.about, name="home"),
    path("services",views.services, name="home"),
    path("contact",views.contact, name="home"),
    path("index",views.index, name="home"),
    
]
