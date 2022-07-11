from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
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
    return render(request,'users/users-register.html',context)

# login view
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/users-login.html',context)

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
            return redirect('users-myprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    classes = request.user.profile.classes.all()
    user_questions = len(request.user.questions.all())
    user_answers = len(request.user.answers.all())
    user_solutions = len(request.user.answers.filter(solution=True))
    context = {
        'title':'My Profile',
        'u_form':u_form,
        'p_form':p_form,
        'classes':classes,
        'user_questions':user_questions,
        'user_answers':user_answers,
        'user_solutions':user_solutions
    }
    return render(request,'users/users-myprofile.html',context)

class MyClassesListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-myclasses.html'
    context_object_name = 'classes'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return profile.classes.all()

class MyProjectsListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-myprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'users/users-project_form.html'
    fields = ['title','blurb','project_link','description']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'users/users-projectdetails.html'

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['title','blurb','project_link','description']
    template_name = 'users/users-project_form.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Project
    template_name = 'users/users-project_confirm_delete.html'
    success_url = reverse_lazy('users-myprojects')

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False