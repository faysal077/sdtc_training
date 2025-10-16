# centers/admin.py
from django.contrib import admin
from .models import Center

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "Center_name",
        "Establishment_year",
        "District",
        "RD_office",
        "Officer_in_charge",
    )
    search_fields = ("Center_name", "District", "RD_office")
    list_filter = ("District", "RD_office")
    ordering = ("Center_name",)
