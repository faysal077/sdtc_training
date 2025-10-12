from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Instructor
from django import forms


# Simple form (no forms.py needed for now)
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            "center_id",
            "type",
            "designation",
            "contact_number",
            "email",
            "education",
            "contract_start_date",
            "contract_end_date",
        ]
        widgets = {
            "contract_start_date": forms.DateInput(attrs={"type": "date"}),
            "contract_end_date": forms.DateInput(attrs={"type": "date"}),
        }


def instructor_list(request):
    instructors = Instructor.objects.all().order_by("-id")
    return render(request, "instructors/instructor_list.html", {"instructors": instructors})



# instructors/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import InstructorForm
from .models import Instructor

def add_instructor(request):
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            instructor = form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "message": "Instructor added successfully!"})
            return redirect("instructors:list")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = InstructorForm()
    return render(request, "instructors/instructor_form.html", {"form": form, "title": "Add Instructor"})


def edit_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    if request.method == "POST":
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = InstructorForm(instance=instructor)
    return render(request, "instructors/instructor_form.html", {"form": form, "title": "Edit Instructor"})


def delete_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    if request.method == "POST":
        instructor.delete()
        return redirect("list")
    return render(request, "instructors/instructor_confirm_delete.html", {"instructor": instructor})


# Create your views here.
