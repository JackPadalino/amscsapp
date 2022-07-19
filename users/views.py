from django.urls.base import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ProjectForm,ProjectVideoForm,ProjectLinkForm,ProjectPhotoForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,ProjectVideo,ProjectPhoto
import re
import os

EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN')
REGISTERED_EMAILS = os.environ.get('REGISTERED_EMAILS')

# view to register a new user
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
        'form':form
    }
    return render(request,'users/users-register.html',context)

# view to log in
def login(request):
    return render(request,'users/users-login.html')

# view to see/update details of a user's profile
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
        'u_form':u_form,
        'p_form':p_form,
        'classes':classes,
        'user_questions':user_questions,
        'user_answers':user_answers,
        'user_solutions':user_solutions
    }
    return render(request,'users/users-my-profile.html',context)

# view to list all projects of a user
class MyClassesListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-my-classes.html'
    context_object_name = 'classes'

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return profile.classes.all()

# view for step 1 of creating a new project
@login_required
def CreateProjectStepOneView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            blurb = form.cleaned_data['blurb']
            description = form.cleaned_data['description']
            project = Project.objects.create(user=user,title=title,blurb=blurb,description=description)
            return redirect('users-create-project-step-2',pk=project.pk)
    else:
        form = ProjectForm()
    context = {
        'form':form
    }
    return render(request,'users/users-create-project-step-1-add-text.html',context)

# view for step 2 of creating a new project
@login_required
def CreateProjectStepTwoView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    user = request.user
    if request.method == 'POST':
        form = ProjectLinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['project_link']
            project.project_link = link
            project.save()
            return redirect('users-create-project-step-3',pk=project.pk)
    else:
        form = ProjectLinkForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/users-create-project-step-2-add-link.html',context)

# view for step 3 of creating a new project
@login_required
def CreateProjectStepThreeView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectVideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.project = project
            video.save()
            return redirect('users-create-project-step-4',pk=project.pk)
    else:
        form = ProjectVideoForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/users-create-project-step-3-add-video.html',context)

# view for step 4 of creating a new project
@login_required
def CreateProjectStepFourView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectPhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.project = project
            photo.save()
            return redirect('users-project-details',pk=project.pk)
    else:
        form = ProjectPhotoForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/users-create-project-step-4-add-photo.html',context)

# view to see the details of a project
class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'users/users-project-details.html'

# view to see all classes for a user
class MyProjectsListView(LoginRequiredMixin,ListView):
    template_name = 'users/users-my-projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

# view to edit the text of a project
class EditProjectTextView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['title','blurb','description']
    template_name = 'users/users-edit-project-edit-text.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

# view to delete a project
class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Project
    template_name = 'users/users-project-confirm-delete.html'
    success_url = reverse_lazy('users-my-projects')

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

# view to edit a project's link
class EditProjectAddLinkView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['project_link']
    template_name = 'users/users-edit-project-add-link.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

# view to add a new project video
@login_required
def EditProjectAddVideoView(request,pk):
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
    return render(request,'users/users-edit-project-add-video.html',context)

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

# view to delete a project video
@login_required
def ProjectVideoDeleteView(request,project_pk,video_pk):
    video  = ProjectVideo.objects.get(pk=video_pk)
    video.delete()
    return redirect('users-project-details',pk=project_pk)

# view to add a new project photo
@login_required
def EditProjectAddPhotoView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectPhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.project = project
            photo.save()
            return redirect('users-project-details',pk=project.pk)
    else:
        form = ProjectPhotoForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/users-edit-project-add-photo.html',context)

# Created function based views for 'project photo confirm delete' and 'project photo delete' instead
# of class-based views as a result of multiple pieces of information needing to be passed into urls and
# templates. Needed a project_pk to be passed in to redirect back to the project-details page after
# deleting a photo, and needed a photo_pk to delete the correct project photo object.
@login_required
def ProjectPhotoConfirmDeleteView(request,project_pk,project_photo_pk):
    context = {
        'project_pk':project_pk,
        'project_photo_pk':project_photo_pk
    }
    return render(request,'users/users-project-photo-confirm-delete.html',context)

# view to delete a project photo
@login_required
def ProjectPhotoDeleteView(request,project_pk,project_photo_pk):
    photo  = ProjectPhoto.objects.get(pk=project_photo_pk)
    photo.delete()
    return redirect('users-project-details',pk=project_pk)