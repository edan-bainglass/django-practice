from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/new', views.registration, name='new_users'),
]
