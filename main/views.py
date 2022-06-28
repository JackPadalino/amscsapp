from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from classroom.models import SchoolYear,Classroom

# Create your views here.
def home(request):
    context = {
        'title':'Home',
    }
    return render(request,'main/home.html',context)

class SchoolYearListView(ListView):
    model = SchoolYear
    template_name = 'main/schoolyears.html'
    context_object_name = 'schoolyears'

'''
    # this function filters Classroom objects by the 'year' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'classes' to the template
    def get_queryset(self):
        self.year = get_object_or_404(SchoolYear, year=self.kwargs['year'])
        return School.objects.filter(school_year=self.year)
    
    # this function is using the string passed in from the URL, turning it into a context
    # variable 'school_year', and then passing that variable into the template to be used
    # as the page's title
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_year'] = self.kwargs['year']
        return context
'''

class ClassesListView(ListView):
    #model = Classroom
    template_name = 'main/classes.html'
    context_object_name = 'classes'

    # this function filters Classroom objects by the 'year' argument passed in from the URL
    # and then returns an 'object_list' that has been renamed to 'classes' to the template
    def get_queryset(self):
        self.school_year = get_object_or_404(SchoolYear, pk=self.kwargs['pk'])
        return Classroom.objects.filter(school_year=self.school_year)

    
    # this function is using the string passed in from the URL, turning it into a context
    # variable 'school_year', and then passing that variable into the template to be used
    # as the page's title
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_year'] = SchoolYear.objects.get(id=self.kwargs['pk'])
        return context
