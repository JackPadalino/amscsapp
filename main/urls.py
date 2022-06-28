from django.urls import path
from . import views
from .views import SchoolYearListView,ClassesListView

urlpatterns = [
    path('',views.home,name='main-home'),
    path('school-year/',SchoolYearListView.as_view(),name='main-school-years'),
    path('school-year/<int:pk>/',ClassesListView.as_view(),name='main-classes'),
]