from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='list'),
    path('add/', views.add_item, name='add'),
    path('<int:item_id>/edit/', views.edit_item, name='edit'),
    path('<int:item_id>/delete/', views.delete_item, name='delete'),
]
