from django.urls import path
from . import views
from .views import ClassDetailView, StudentProfileListView,StudentDetailsView,ProjectDetailView

urlpatterns = [
    path('<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='classroom-classroom-main'),
    path('<str:class_title>/<int:pk>/meet-the-team/',StudentProfileListView.as_view(),name='classroom-classroom-profiles'),
    path('<int:pk>/student-details/',StudentDetailsView,name='classroom-studentdetails'),
    path('projectdetails/<int:pk>',ProjectDetailView.as_view(),name='classroom-projectdetails'),
]