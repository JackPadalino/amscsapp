from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ProjectVideoForm,ProjectLinkForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,ProjectVideo
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
            return redirect('users-my-profile')
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
    return render(request,'users/users-my-profile.html',context)

class MyClassesListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-my-classes.html'
    context_object_name = 'classes'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return profile.classes.all()

class MyProjectsListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-my-projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'users/users-project_form.html'
    fields = ['title','blurb','description']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'users/users-project-details.html'
    #context_object_name = 'videos'
    
    #def get_queryset(self):
    #    self.project = get_object_or_404(Project,pk=self.kwargs['pk'])
    #    return self.project.project_videos.all()

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['title','blurb','description']
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
    success_url = reverse_lazy('users-my-projects')

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

class AddProjectLinkView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['project_link']
    template_name = 'users/users-add-link.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

@login_required
def AddProjectVideoView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectVideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.project = project
            video.save()
            return redirect('users-project-details',pk=project.pk)
    else:
        form = ProjectVideoForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/users-add-video.html',context)

 # Created function based views for 'project video confirm delete' and 'project video delete' instead
 # of class-based views as a result of multiple pieces of information needing to be passed into urls and
 # templates. Needed a project_pk to be passed in to redirect back to the project-details page after
 # deleting a video, and needed a video_pk to delete the correct project video object.
@login_required
def ProjectVideoConfirmDeleteView(request,project_pk,video_pk):
    context = {
        'project_pk':project_pk,
        'video_pk':video_pk
    }
    return render(request,'users/users-project-video-confirm-delete.html',context)

@login_required
def ProjectVideoDeleteView(request,project_pk,video_pk):
    video  = ProjectVideo.objects.get(pk=video_pk)
    video.delete()
    return redirect('users-project-details',pk=project_pk)