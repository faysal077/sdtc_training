from django.urls import path
from . import views

app_name = "participants"

urlpatterns = [
    # AJAX add participant
    path("add/<int:batch_id>/", views.participant_add_ajax, name="participant_add_ajax"),

    # Detail and edit
    path("<int:pk>/", views.ParticipantDetailView.as_view(), name="participant_detail"),
    path("<int:pk>/edit/", views.ParticipantUpdateView.as_view(), name="participant_edit"),

    # Uncomment if you implement JobHistory or toggle employment
    # path("<int:pk>/job-history/add/", views.JobHistoryCreateView.as_view(), name="jobhistory_add"),
    # path("<int:pk>/employment-toggle/", views.toggle_employment_status, name="employment_toggle"),
]
