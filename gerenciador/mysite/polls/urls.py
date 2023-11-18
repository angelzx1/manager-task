from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login),
    path('create-task', views.createTask),
    path('view-tasks', views.viewTasks, name='view-tasks'),
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    ]
