from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login
from .models import CustomUser

def verify_email(request, uid, token):
    user = CustomUser.objects.get(pk=uid)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('products/home')
    return render(request, 'email_invalid.html')
