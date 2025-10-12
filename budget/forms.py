# budget/forms.py
from django import forms
from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['center_id', 'name', 'echonomic_code', 'description', 'allocation', 'achivement', 'requirement']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Budget Name'}),
            'echonomic_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Economic Code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Optional Description'}),
            'allocation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Allocation'}),
            'achivement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achievement'}),
            'requirement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requirement'}),
            'center_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Center ID'}),
        }
