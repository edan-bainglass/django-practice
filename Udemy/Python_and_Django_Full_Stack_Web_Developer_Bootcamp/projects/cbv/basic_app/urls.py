from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path(
        '',
        views.SchoolListView.as_view(),
        name='list',
    ),
    path(
        '<int:pk>/',
        views.SchoolDetailView.as_view(),
        name='detail',
    ),
    path(
        'create/',
        views.SchoolCreateView.as_view(),
        name='create',
    ),
    path(
        'update/<int:pk>/',
        views.SchoolUpdateView.as_view(),
        name='update',
    ),
    path(
        'delete/<int:pk>/',
        views.SchoolDeleteView.as_view(),
        name='delete',
    ),
    path('update/<int:pk>/student/create/',
         views.StudentCreateView.as_view(),
         name='create_student'),
    path('update/<int:pk>/student/update/<int:student_pk>/',
         views.StudentUpdateView.as_view(),
         name='update_student'),
    path('update/<int:pk>/student/delete/<int:student_pk>/',
         views.StudentDeleteView.as_view(),
         name='delete_student'),
]
