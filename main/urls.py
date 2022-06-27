from django.urls import path
from . import views
from .views import ClassesListView

urlpatterns = [
    path('',views.home,name='main-home'),
    path('<str:year>/',ClassesListView.as_view(),name='main-classes'),
]