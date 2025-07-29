
from django.urls import path
from . import views
from django.shortcuts import render
from . import views

urlpatterns = [
     path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),

    path('login_profile/',views.login_profile_view, name='login_profile'),
    path('register/',views.signup_view, name='signup'),
]
