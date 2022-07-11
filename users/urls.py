from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .views import MyClassesListView,ProjectCreateView,MyProjectsListView,ProjectDetailView,ProjectDeleteView,ProjectUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='users-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/users-login.html'),name='users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/users-logout.html'),name='users-logout'),
    path('myprofile/',views.profile,name='users-myprofile'),
    path('myclasses/',MyClassesListView.as_view(),name='users-myclasses'),
    path('myprojects/',MyProjectsListView.as_view(),name='users-myprojects'),
    path('createproject/',ProjectCreateView.as_view(),name='users-createproject'),
    path('projectdetails/<int:pk>',ProjectDetailView.as_view(),name='users-projectdetails'),
    path('updateproject/<int:pk>',ProjectUpdateView.as_view(),name='users-updateproject'),
    path('deleteproject/<int:pk>/',ProjectDeleteView.as_view(),name='users-deleteproject'),
    #path('account/<int:pk>/delete/',UserDeleteView.as_view(),name='account-delete'),
    #path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    #path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    #path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]