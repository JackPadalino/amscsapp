from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from .models import SchoolYear,Classroom
from users.models import Profile,Project
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
    return render(request,'classroom/classroom-studentdetails.html',context)

#class ProjectDetailView(LoginRequiredMixin,DetailView):
#    model = Project
#    template_name = 'classroom/classroom-projectdetails.html'

@login_required
def ProjectDetailView(request,profile_pk,project_pk):
    profile = Profile.objects.get(pk=profile_pk)
    project = Project.objects.get(pk=project_pk)
    context = {
        'profile':profile,
        'project':project
    }
    return render(request,'classroom/classroom-projectdetails.html',context)