from django.urls import path, include 
from . import views

urlpatterns = [
    path('',views.index),#login
    path('user/registration',views.registration),#register
]