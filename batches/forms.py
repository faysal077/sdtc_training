from django import forms
from .models import Batch

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            "Center_id",
            "Course_id",
            "Fiscal_year",
            "Participant_target",
            "Course_target",
            "Proposed_start_date",
            "Proposed_end_date",
            "Actual_start_date",
            "Actual_end_date",
        ]
        widgets = {
            "Fiscal_year": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "Proposed_start_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "Proposed_end_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "Actual_start_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "Actual_end_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }
