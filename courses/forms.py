from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["Center_id", "Course_name", "Course_duration", "Batch_number"]
        widgets = {
            "Course_name": forms.TextInput(attrs={"class": "form-control"}),
            "Course_duration": forms.TextInput(attrs={"class": "form-control"}),
            "Batch_number": forms.NumberInput(attrs={"class": "form-control"}),
            # Center_id is readonly because it will be auto-filled
            "Center_id": forms.NumberInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }
