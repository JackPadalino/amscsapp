from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from users.views import login
from .models import SchoolYear,Classroom
from users.models import Profile,Project,ProjectComment
from users.forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import JoinClassForm

# view to see the details of a classroom
class ClassDetailView(LoginRequiredMixin,DetailView):
    template_name = 'classroom/classroom-main.html'
    model = Classroom
    context_object_name = 'classroom'

# view to see the list of student profiles in a classroom
class StudentProfileListView(LoginRequiredMixin,ListView):
    template_name = 'classroom/classroom-profiles.html'
    model = Classroom
    context_object_name = 'profiles'

    # this function filters Classroom objects by the 'pk' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'profiles' which is then returned 
    # to the template
    def get_queryset(self):
        self.classroom = get_object_or_404(Classroom, pk=self.kwargs['pk'])
        return self.classroom.profiles.all()

# view to see the details of a student's profile
@login_required
def StudentDetailsView(request,pk):
    profile = Profile.objects.get(pk=pk)
    classrooms = profile.classes.all()
    projects = Project.objects.filter(user=profile.user)
    context = {
        'profile':profile,
        'classrooms':classrooms,
        'projects':projects
    }
    return render(request,'classroom/classroom-student-details.html',context)

# view to see the details of a project
@login_required
def ProjectDetailView(request,profile_pk,project_pk):
    user=request.user
    profile = Profile.objects.get(pk=profile_pk)
    project = Project.objects.get(pk=project_pk)
    comments = ProjectComment.objects.filter(project=project)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.author = user
            comment.save()
            return redirect('classroom-project-details',profile_pk=profile.pk,project_pk=project.pk)
    else:
        comment_form = CommentForm()
    context = {
        'profile':profile,
        'project':project,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'classroom/classroom-project-details.html',context)

# view to update a project comment
class ProjectCommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ProjectComment
    fields = ['content']
    template_name = 'classroom/classroom-update-comment.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if comment.author == self.request.user:
            return True
        return False

# view to delete a project comment
class ProjectCommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = ProjectComment
    template_name = 'classroom/classroom-project-comment-confirm-delete.html'

    def get_success_url(self):
        return reverse_lazy( 'classroom-project-details', kwargs={'profile_pk': self.object.project.user.profile.id,'project_pk':self.object.project.pk})

    def test_func(self):
        comment = self.get_object()
        if comment.author == self.request.user:
            return True
        return False

# view to join a class
def JoinClassView(request,classroom_pk):
    user = request.user
    profile = Profile.objects.get(user=user)
    classroom = Classroom.objects.get(pk=classroom_pk)
    if request.method == 'POST':
        form = JoinClassForm(request.POST)
        if form.is_valid():
            join_code = form.cleaned_data['join_code']
            if join_code == classroom.join_code:
                if profile not in classroom.profiles.all():
                    classroom.profiles.add(profile)
                    messages.add_message(request,messages.SUCCESS,'You have been added to this class. Welcome to the team!')
                else:
                    messages.add_message(request,messages.SUCCESS,'Looks like you are already in this class!')
                return redirect('classroom-classroom-main',class_title=classroom.title,pk=classroom.pk)
            else:
                messages.add_message(request,messages.ERROR,'Oops! Something went wrong. Maybe you entered the wrong join code?')       
    else:
        form = JoinClassForm()
    context = {
        'form':form
    }
    return render(request, 'classroom/classroom-join-class.html', context)