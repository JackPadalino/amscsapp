from django.urls import path
from . import views
from .views import SchoolYearListView,ClassesListView

urlpatterns = [
    path('',views.home,name='main-home'),
    path('find-classes/',SchoolYearListView.as_view(),name='main-school-years'),
    path('find-classes/school-year/<int:pk>/',ClassesListView.as_view(),name='main-classes'),
]