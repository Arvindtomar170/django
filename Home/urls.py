from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('servises', views.servises,name='servises'),
    path('contact', views.contact,name='contact'),
    path('index', views.index,name='index'),
]
