
from django.urls import path
from django.urls import include

from userApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name='userApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userApp/logout.html'), name='logout'),

]
