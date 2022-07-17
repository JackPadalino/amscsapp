from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.views import login
from .models import SchoolYear,Classroom
from users.models import Profile,Project,ProjectComment
from users.forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ClassDetailView(LoginRequiredMixin,DetailView):
    template_name = 'classroom/classroom-main.html'
    model = Classroom
    context_object_name = 'classroom'

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

#class ProjectDetailView(LoginRequiredMixin,DetailView):
#    model = Project
#    template_name = 'classroom/classroom-projectdetails.html'

@login_required
def ProjectDetailView(request,profile_pk,project_pk):
    user=request.user
    profile = Profile.objects.get(pk=profile_pk)
    project = Project.objects.get(pk=project_pk)
    comments = ProjectComment.objects.filter(project=project)
    comment_form = CommentForm()
    if request.method == 'POST':
        #if 'commentbutton' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.author = user
            comment.save()
            return redirect('classroom-project-details',profile_pk=profile.pk,project_pk=project.pk)
    context = {
        'profile':profile,
        'project':project,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'classroom/classroom-project-details.html',context)

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

class ProjectCommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = ProjectComment
    template_name = 'classroom/classroom-project_comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy( 'classroom-project-details', kwargs={'profile_pk': self.object.project.user.profile.id,'project_pk':self.object.project.pk})

    def test_func(self):
        comment = self.get_object()
        if comment.author == self.request.user:
            return True
        return False