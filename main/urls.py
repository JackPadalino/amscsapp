from django.urls import path
from . import views
from .views import ClassesView

urlpatterns = [
    path('',views.home,name='main-home'),
    path('classes/<str:year>/',ClassesView.as_view(),name='main-classes')
]