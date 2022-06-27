from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView

# Create your views here.
def home(request):
    context = {
        'title':'Home',
    }
    return render(request,'main/home.html',context)