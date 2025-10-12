# instructors/forms.py
from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'center_id',
            'type',
            'designation',
            'contact_number',
            'email',
            'education',
            'contract_start_date',
            'contract_end_date',
        ]
        widgets = {
            'center_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Center ID'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Instructor Type'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Educational Qualification'}),
            'contract_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contract_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
