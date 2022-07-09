from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from .models import SchoolYear,Classroom
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ClassDetailView(LoginRequiredMixin,DetailView):
    template_name = 'classroom/classroom-main.html'
    model = Classroom
    context_object_name = 'classroom'

class StudentProfileListView(ListView):
    template_name = 'classroom/classroom-profiles.html'
    model = Classroom
    context_object_name = 'profiles'

    # this function filters Classroom objects by the 'pk' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'profiles' which is then returned 
    # to the template
    def get_queryset(self):
        self.classroom = get_object_or_404(Classroom, pk=self.kwargs['pk'])
        return self.classroom.profiles.all()