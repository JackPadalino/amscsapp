from django.urls import path
from . import views
from .views import ClassesListView,ClassDetailView

urlpatterns = [
    path('',views.home,name='main-home'),
    path('classes/<str:year>/',ClassesListView.as_view(),name='main-classes'),
    path('classes/<str:year>/<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='main-class-page')
]