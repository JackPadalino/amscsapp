from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Classroom

# Create your views here.
class ClassDetailView(DetailView):
    template_name = 'classroom/classroom.html'
    model = Classroom
    context_object_name = 'classroom'