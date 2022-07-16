from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    MyClassesListView,
    ProjectCreateView,
    MyProjectsListView,
    ProjectDetailView,
    ProjectDeleteView,
    ProjectUpdateView,
    AddProjectVideoView,
    ProjectVideoConfirmDeleteView,
    ProjectVideoDeleteView,
    AddProjectLinkView
    )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='users-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/users-login.html'),name='users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/users-logout.html'),name='users-logout'),
    path('my-profile/',views.profile,name='users-my-profile'),
    path('my-classes/',MyClassesListView.as_view(),name='users-my-classes'),
    path('my-projects/',MyProjectsListView.as_view(),name='users-my-projects'),
    path('create-project/',ProjectCreateView.as_view(),name='users-create-project'),
    path('project-details/<int:pk>',ProjectDetailView.as_view(),name='users-project-details'),
    path('update-project/<int:pk>',ProjectUpdateView.as_view(),name='users-update-project'),
    path('delete-project/<int:pk>/',ProjectDeleteView.as_view(),name='users-delete-project'),
    path('add-video/<int:pk>/',AddProjectVideoView,name='users-add-video'),
    path('add-link/<int:pk>/',AddProjectLinkView.as_view(),name='users-add-link'),
    path('confirm-delete-video/<int:project_pk>/<int:video_pk>/',ProjectVideoConfirmDeleteView,name='users-confirm-delete-video'),
    path('delete-video/<int:project_pk>/<int:video_pk>/',ProjectVideoDeleteView,name='users-delete-video')
    #path('account/<int:pk>/delete/',UserDeleteView.as_view(),name='account-delete'),
    #path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    #path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    #path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]