from django.urls import path
from . import views
from .views import ClassesListView,ClassDetailView

urlpatterns = [
    path('<str:class_title>/<int:pk>/',ClassDetailView.as_view(),name='classroom-classroom-main')
]