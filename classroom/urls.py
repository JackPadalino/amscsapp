from django.urls import path
from . import views
from .views import ClassDetailView, StudentProfileListView,StudentDetailsView,ProjectDetailView,ProjectCommentUpdateView,ProjectCommentDeleteView
#from users.views import ProjectDetailView

urlpatterns = [
    path('class-details/<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='classroom-classroom-main'),
    path('class-details/meet-the-team/<str:class_title>/<int:pk>/',StudentProfileListView.as_view(),name='classroom-classroom-profiles'),
    path('student-details/<int:pk>/',StudentDetailsView,name='classroom-student-details'),
    path('project-details/<int:profile_pk>/<int:project_pk>/',ProjectDetailView,name='classroom-project-details'),
    path('edit-comment/<int:pk>/',ProjectCommentUpdateView.as_view(),name='classroom-update-comment'),
    path('delete-comment/<int:pk>/',ProjectCommentDeleteView.as_view(),name='classroom-delete-comment'),
]