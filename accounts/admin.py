# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class AccountAdmin(UserAdmin):
    # Fields to display in the admin list
    list_display = ("username", "center", "is_staff", "is_superuser")

    # Fields to search
    search_fields = ("username", "center__Center_name", "center__District")

    # Fields to filter by (right sidebar)
    list_filter = ("is_staff", "is_superuser", "center__District")

    # Fields shown when editing or adding
    fieldsets = (
        (None, {"fields": ("username", "password", "center")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "center", "is_staff", "is_superuser"),
        }),
    )

    ordering = ("username",)

