from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.budget_list, name='list'),
    path('add/', views.add_budget, name='add'),
    path('<int:budget_id>/edit/', views.edit_budget, name='edit'),
    path('<int:budget_id>/delete/', views.delete_budget, name='delete'),
]
