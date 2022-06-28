from cProfile import Profile
from django.urls.base import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile
import re
import os

EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN')
REGISTERED_EMAILS = os.environ.get('REGISTERED_EMAILS')

# register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email_domain = re.search("@[\w.]+", email)
            if email_domain.group() == EMAIL_DOMAIN:
            #if email in REGISTERED_EMAILS:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f'Account created for {username}! You are now able to sign in.')
                return redirect('users-login')
            else:
                messages.error(request,f'Sorry. You are not authorized to register.')
    else:
        form = UserRegisterForm()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)

# login view
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)

# profile details/update view
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account information has been updated.')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    classes = request.user.profile.classes.all()
    context = {
        'title':'My Profile',
        'u_form':u_form,
        'p_form':p_form,
        'classes':classes
    }
    return render(request,'users/profile.html',context)