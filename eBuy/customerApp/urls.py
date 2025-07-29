
from django.urls import path
from .views import verify_email
from django.contrib.auth.views import LogoutView
from django.shortcuts import render

urlpatterns = [
    path('verify/<int:uid>/<str:token>/', verify_email, name='verify_email'),
    path('', lambda request: render(request, 'home.html'), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
