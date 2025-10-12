# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Account


def login_view(request):
    """
    Custom login view using Account model authentication.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        # inside accounts/views.py, in login_view()
        if user is not None:
            login(request, user)
            # store extra session info (optional)
            request.session["center_id"] = user.center.id if user.center else None
            request.session["district"] = user.center.District if user.center else None
            request.session["is_superuser"] = user.is_superuser
            return redirect("dashboard")  # ✅ changed

        # if user is not None:
        #     login(request, user)
        #     # store extra session info
        #     request.session["center_id"] = user.center.id if user.center else None
        #     request.session["center_name"] = user.center.Center_name if user.center else None
        #     request.session["district"] = user.center.District if user.center else None
        #     request.session["is_superuser"] = user.is_superuser
        #
        #     messages.success(request, f"Welcome {user.username}!")
        #     return redirect("accounts:profile")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


@login_required(login_url="accounts:login")
def profile(request):
    """
    Profile/dashboard page after login
    """
    center_id = request.session.get("center_id")
    center_name = request.session.get("center_name")
    district = request.session.get("district")
    is_superuser = request.session.get("is_superuser", False)

    return render(
        request,
        "accounts/profile.html",
        {
            "center_id": center_id,
            "center_name": center_name,
            "district": district,
            "is_superuser": is_superuser,
        },
    )


def logout_view(request):
    """
    Logs out user and clears session
    """
    logout(request)
    request.session.flush()  # clear custom session data
    return redirect("accounts:login")
