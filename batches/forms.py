from django import forms
from .models import Batch

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            "Center_id",
            "Course_id",
            "Participant_target",
            "Course_target",
            "Proposed_start_date",
            "Proposed_end_date",
            "Actual_start_date",
            "Actual_end_date",
            "Fiscal_year",  # Fiscal year moved to the end
        ]
        widgets = {
            "Center_id": forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
            "Course_id": forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
            "Fiscal_year": forms.TextInput(attrs={
                "class": "form-control",
                "readonly": "readonly",
                "placeholder": "Auto-calculated (June–July)"
            }),

            "Participant_target": forms.NumberInput(attrs={"class": "form-control"}),
            "Course_target": forms.NumberInput(attrs={"class": "form-control"}),

            "Proposed_start_date": forms.DateInput(attrs={
                "type": "date", "class": "form-control"
            }),
            "Proposed_end_date": forms.DateInput(attrs={
                "type": "date", "class": "form-control"
            }),
            "Actual_start_date": forms.DateInput(attrs={
                "type": "date", "class": "form-control"
            }),
            "Actual_end_date": forms.DateInput(attrs={
                "type": "date", "class": "form-control"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mark Fiscal_year as not required since it’s auto-calculated
        self.fields["Fiscal_year"].required = False
