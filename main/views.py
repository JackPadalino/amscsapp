from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from classroom.models import SchoolYear,Classroom
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def home(request):
    context = {
        'title':'Home',
    }
    return render(request,'main/home.html',context)

class SchoolYearListView(LoginRequiredMixin,ListView):
    model = SchoolYear
    template_name = 'main/classbyschoolyear.html'
    context_object_name = 'schoolyears'

class ClassesListView(LoginRequiredMixin,ListView):
    template_name = 'main/classes.html'
    context_object_name = 'classes'

    # this function filters Classroom objects by the 'year' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'classes' to the template
    def get_queryset(self):
        self.school_year = get_object_or_404(SchoolYear, pk=self.kwargs['pk'])
        return Classroom.objects.filter(school_year=self.school_year)

    # this function is using the pk passed in from the URL to create a variable 'school_year'
    # that will be passed into the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_year'] = SchoolYear.objects.get(id=self.kwargs['pk'])
        return context