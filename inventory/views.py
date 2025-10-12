from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Inventory


# Django ModelForm for Inventory
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["center_id", "name", "description", "category", "condition", "quantity"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }


def inventory_list(request):
    items = Inventory.objects.all().order_by("-id")
    return render(request, "inventory/inventory_list.html", {"items": items})


from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Inventory
from django import forms

# Create form directly in views.py since you don't have forms.py
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["center_id", "name", "description", "category", "condition", "quantity"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "condition": forms.TextInput(attrs={"class": "form-control"}),
            "center_id": forms.NumberInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }

def add_item(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "message": "✅ Item saved successfully!"})
            return redirect("inventory:list")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = InventoryForm()
    return render(request, "inventory/inventory_form.html", {"form": form, "title": "Add Inventory Item"})




def edit_item(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = InventoryForm(instance=item)
    return render(request, "inventory/inventory_form.html", {"form": form, "title": "Edit Item"})


def delete_item(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("list")
    return render(request, "inventory/inventory_confirm_delete.html", {"item": item})

