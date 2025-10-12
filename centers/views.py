# centers/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Center
from accounts.models import Account

def center_list(request):
    """
    List all centers. Normal users see only their district.
    Super Admin sees all centers.
    """
    is_superuser = request.session.get("is_superuser", False)
    district = request.session.get("district")

    if is_superuser:
        centers = Center.objects.all().order_by("Center_name")
    else:
        centers = Center.objects.filter(District=district).order_by("Center_name")

    return render(request, "centers/center_list.html", {"centers": centers})


def add_center(request):
    """
    Add a new center, optionally with a linked user account.
    """
    if request.method == "POST":
        center_name = request.POST.get("Center_name")
        establishment_year = request.POST.get("Establishment_year")
        district = request.POST.get("District")
        rd_office = request.POST.get("RD_office")
        officer = request.POST.get("Officer_in_charge")

        center = Center.objects.create(
            Center_name=center_name,
            Establishment_year=establishment_year,
            District=district,
            RD_office=rd_office,
            Officer_in_charge=officer,
        )

        # Optionally create a user account for this center
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_superuser = request.POST.get("is_superuser") == "on"

        if username and password:
            Account.objects.create_user(
                username=username,
                password=password,
                center=center,
                is_superuser=is_superuser,
                is_staff=is_superuser,  # required for Django admin
            )

        messages.success(request, "Center added successfully!")
        return redirect("list")

    return render(request, "centers/add_center.html")


def edit_center(request, center_id):
    """
    Edit an existing center
    """
    center = get_object_or_404(Center, id=center_id)

    if request.method == "POST":
        center.Center_name = request.POST.get("Center_name")
        center.Establishment_year = request.POST.get("Establishment_year")
        center.District = request.POST.get("District")
        center.RD_office = request.POST.get("RD_office")
        center.Officer_in_charge = request.POST.get("Officer_in_charge")
        center.save()

        messages.success(request, "Center updated successfully!")
        return redirect("list")

    return render(request, "centers/edit_center.html", {"center": center})


def delete_center(request, center_id):
    """
    Delete a center and its linked accounts
    """
    center = get_object_or_404(Center, id=center_id)

    if request.method == "POST":
        # Delete accounts linked to this center
        Account.objects.filter(center=center).delete()
        center.delete()
        messages.success(request, "Center and linked accounts deleted successfully!")
        return redirect("list")

    return render(request, "centers/delete_center.html", {"center": center})
