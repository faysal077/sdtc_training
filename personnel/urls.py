from django.urls import path
from . import views

app_name = 'personnel'

urlpatterns = [
    path('', views.personnel_list, name='list'),
    path('add/', views.add_personnel, name='add'),
    path('<int:person_id>/edit/', views.edit_personnel, name='edit'),
    path('<int:person_id>/delete/', views.delete_personnel, name='delete'),
]
