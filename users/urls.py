from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    EditProjectAddLinkView,
    EditProjectAddPhotoView,
    EditProjectAddVideoView,
    EditProjectTextView,
    MyClassesListView,
    #ProjectCreateView,
    MyProjectsListView,
    ProjectDetailView,
    ProjectDeleteView,
    EditProjectTextView,
    EditProjectAddVideoView,
    ProjectVideoConfirmDeleteView,
    ProjectVideoDeleteView,
    EditProjectAddLinkView,
    EditProjectAddPhotoView,
    ProjectPhotoConfirmDeleteView,
    ProjectPhotoDeleteView,
    CreateProjectStepOneView,
    CreateProjectStepTwoView,
    CreateProjectStepThreeView,
    CreateProjectStepFourView,
    CreateProjectStepFiveView,
    )

urlpatterns = [
    path('register/',views.register,name='users-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/users-login.html'),name='users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/users-logout.html'),name='users-logout'),
    path('my-profile/',views.profile,name='users-my-profile'),
    path('my-classes/',MyClassesListView.as_view(),name='users-my-classes'),
    #path('create-project-step-1/',CreateProjectStepOneView,name='users-create-project-step-1'),
    #path('create-project-step-2/<int:pk>/',CreateProjectStepTwoView,name='users-create-project-step-2'),
    #path('create-project-step-3/<int:pk>/',CreateProjectStepThreeView,name='users-create-project-step-3'),
    #path('create-project-step-4/<int:pk>/',CreateProjectStepFourView,name='users-create-project-step-4'),
    path('create-project-step-1/',CreateProjectStepOneView,name='users-create-project-step-1'),
    path('create-project-step-2/<int:temp_project_pk>/',CreateProjectStepTwoView,name='users-create-project-step-2'),
    path('create-project-step-3/<int:temp_project_pk>/',CreateProjectStepThreeView,name='users-create-project-step-3'),
    path('create-project-step-4/<int:temp_project_pk>/',CreateProjectStepFourView,name='users-create-project-step-4'),
    path('create-project-step-5/<int:temp_project_pk>/',CreateProjectStepFiveView,name='users-create-project-step-5'),
    path('project-details/<int:pk>/',ProjectDetailView,name='users-project-details'),
    path('my-projects/',MyProjectsListView.as_view(),name='users-my-projects'),
    path('edit-project-text/<int:pk>/',EditProjectTextView.as_view(),name='users-update-project'),
    path('add-project-video/<int:pk>/',EditProjectAddVideoView,name='users-add-video'),
    path('add-project-link/<int:pk>/',EditProjectAddLinkView.as_view(),name='users-add-link'),
    path('add-project-photo/<int:pk>/',EditProjectAddPhotoView,name='users-add-project-photo'),
    path('delete-project/<int:pk>/',ProjectDeleteView.as_view(),name='users-delete-project'),
    path('confirm-delete-video/<int:project_pk>/<int:video_pk>/',ProjectVideoConfirmDeleteView,name='users-confirm-delete-video'),
    path('delete-project-video/<int:project_pk>/<int:video_pk>/',ProjectVideoDeleteView,name='users-delete-video'),
    path('confirm-delete-project-photo/<int:project_pk>/<int:project_photo_pk>/',ProjectPhotoConfirmDeleteView,name='users-confirm-delete-project-photo'),
    path('delete-project-photo/<int:project_pk>/<int:project_photo_pk>/',ProjectPhotoDeleteView,name='users-delete-project-photo'),
]