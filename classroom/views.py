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