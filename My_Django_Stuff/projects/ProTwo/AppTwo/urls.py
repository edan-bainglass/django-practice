from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/new', views.new_users, name='new_users'),
    path('help/', views.help, name='help'),
]
