from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import PersonalInfo


# Django ModelForm for PersonalInfo
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ["center_id", "name", "designation", "office", "contact_number", "email"]


def personnel_list(request):
    personnel = PersonalInfo.objects.all().order_by("name")
    return render(request, "personnel/personnel_list.html", {"personnel": personnel})


def add_personnel(request):
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = PersonalInfoForm()
    return render(request, "personnel/personnel_form.html", {"form": form, "title": "Add Personnel"})


def edit_personnel(request, person_id):
    person = get_object_or_404(PersonalInfo, id=person_id)
    if request.method == "POST":
        form = PersonalInfoForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = PersonalInfoForm(instance=person)
    return render(request, "personnel/personnel_form.html", {"form": form, "title": "Edit Personnel"})


def delete_personnel(request, person_id):
    person = get_object_or_404(PersonalInfo, id=person_id)
    if request.method == "POST":
        person.delete()
        return redirect("list")
    return render(request, "personnel/personnel_confirm_delete.html", {"person": person})

