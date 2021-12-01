from django.contrib import admin
from django.urls import path
from django.urls import include

from todolist_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todolist/', views.todolist, name='todolist'),

    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),

    path('completed/<int:id>/', views.completed_task, name='completed_task'),
    path('pending/<int:id>/', views.pending_task, name='pending_task'),

    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us')

]
