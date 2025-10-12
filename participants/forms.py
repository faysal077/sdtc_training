from django import forms
from .models import Participant, JobHistory


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            "center_id",
            "course_id",
            "batch_id",
            "name",
            "father_name",
            "gender",
            "nid",
            "birth_reg",
            "contact_number",
            "email",
            "educational_qualification",
            "date_of_birth",
            "job_status",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }


class JobHistoryForm(forms.ModelForm):
    class Meta:
        model = JobHistory
        fields = ["company_name", "designation", "start_date", "end_date", "currently_employed"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
