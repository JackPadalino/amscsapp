from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from .models import SchoolYear,Classroom

class ClassesListView(ListView):
    template_name = 'main/classes.html'
    context_object_name = 'classes'

    # this function filters Classroom objects by the 'year' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'classes' to the template
    def get_queryset(self):
        self.year = get_object_or_404(SchoolYear, year=self.kwargs['year'])
        return Classroom.objects.filter(school_year=self.year)
    
    # this function is using the string passed in from the URL, turning it into a context
    # variable 'school_year', and then passing that variable into the template to be used
    # as the page's title
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_year'] = self.kwargs['year']
        return context

# Create your views here.
class ClassDetailView(DetailView):
    template_name = 'classroom/classroom-main.html'
    model = Classroom
    context_object_name = 'classroom'