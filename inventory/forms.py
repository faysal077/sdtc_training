# inventory/forms.py
from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["center_id", "name", "description", "category", "condition", "quantity"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "category": forms.TextInput(attrs={"placeholder": "e.g., Electronics"}),
            "condition": forms.TextInput(attrs={"placeholder": "e.g., New / Used"}),
        }
