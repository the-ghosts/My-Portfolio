from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project_app/', views.all_projects, name='all_projects'),
]