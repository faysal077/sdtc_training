# sdtc_training/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account


@login_required
def dashboard_view(request):
    """
    Role-based Dashboard view:
    - Superuser sees all centers
    - Regular user sees only their district’s data
    """
    user = request.user

    # For superuser (admin) — show everything
    if user.is_superuser:
        centers = user.__class__.objects.select_related("center").all()
        return render(request, "dashboard.html", {
            "role": "admin",
            "centers": centers,
        })

    # For normal user — show only their district
    if user.center:
        district = user.center.District
        return render(request, "dashboard.html", {
            "role": "user",
            "district": district,
            "center_name": user.center.Center_name,
        })
    else:
        # If user has no center assigned, redirect to profile
        return redirect("accounts:profile")
