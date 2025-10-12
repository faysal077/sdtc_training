from django.urls import path
from . import views

app_name = 'centers'

urlpatterns = [
    path('', views.center_list, name='list'),
    path('add/', views.add_center, name='add'),
    path('<int:center_id>/edit/', views.edit_center, name='edit'),
    path('<int:center_id>/delete/', views.delete_center, name='delete'),
]
