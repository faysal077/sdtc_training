from django.urls import path
from . import views

app_name = 'participants'
urlpatterns = [
    path('', views.ParticipantListView.as_view(), name='participant_list'),
    path('add/', views.ParticipantCreateView.as_view(), name='participant_add'),
    path('<int:pk>/', views.ParticipantDetailView.as_view(), name='participant_detail'),
    path('<int:pk>/edit/', views.ParticipantUpdateView.as_view(), name='participant_edit'),
    path('<int:pk>/job-history/add/', views.JobHistoryCreateView.as_view(), name='jobhistory_add'),
    path('<int:pk>/employment-toggle/', views.toggle_employment_status, name='employment_toggle'),  # AJAX
]
