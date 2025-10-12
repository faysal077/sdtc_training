from django.urls import path
from . import views

app_name = 'batches'
urlpatterns = [
    path('', views.BatchListView.as_view(), name='batch_list'),
    path('add/', views.BatchCreateView.as_view(), name='batch_add'),
    path('<int:pk>/', views.BatchDetailView.as_view(), name='batch_detail'),
    path('<int:pk>/participants/', views.BatchParticipantsView.as_view(), name='batch_participants'),
]
