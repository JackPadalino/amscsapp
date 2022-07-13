from django.urls import path
from . import views
from .views import ClassDetailView, StudentProfileListView,StudentDetailsView,ProjectDetailView
#from users.views import ProjectDetailView

urlpatterns = [
    path('<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='classroom-classroom-main'),
    path('<str:class_title>/<int:pk>/meet-the-team/',StudentProfileListView.as_view(),name='classroom-classroom-profiles'),
    path('<int:pk>/student-details/',StudentDetailsView,name='classroom-studentdetails'),
    #path('project-details/<int:pk>',ProjectDetailView.as_view(),name='users-project-details'),
    path('projectdetails/<int:profile_pk>/<int:project_pk>/',ProjectDetailView,name='classroom-projectdetails'),
]