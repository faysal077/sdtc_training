from django.urls import path
from . import views

app_name = 'instructors'

urlpatterns = [
    path('', views.instructor_list, name='list'),
    path('add/', views.add_instructor, name='add'),
    path('<int:instructor_id>/edit/', views.edit_instructor, name='edit'),
    path('<int:instructor_id>/delete/', views.delete_instructor, name='delete'),
]
