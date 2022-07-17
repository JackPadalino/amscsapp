from django.urls import path
from . import views
from .views import ClassDetailView, StudentProfileListView,StudentDetailsView,ProjectDetailView,ProjectCommentUpdateView,ProjectCommentDeleteView
#from users.views import ProjectDetailView

urlpatterns = [
    path('<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='classroom-classroom-main'),
    path('<str:class_title>/<int:pk>/meet-the-team/',StudentProfileListView.as_view(),name='classroom-classroom-profiles'),
    path('<int:pk>/student-details/',StudentDetailsView,name='classroom-student-details'),
    #path('project-details/<int:pk>',ProjectDetailView.as_view(),name='users-project-details'),
    path('project-details/<int:profile_pk>/<int:project_pk>/',ProjectDetailView,name='classroom-project-details'),
    path('<int:pk>/edit-comment/',ProjectCommentUpdateView.as_view(),name='classroom-update-comment'),
    path('<int:pk>/delete-comment/',ProjectCommentDeleteView.as_view(),name='classroom-delete-comment'),
]