from django.contrib import admin
from .models import Batch

# ✅ Use decorator correctly — followed immediately by class definition
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    # Columns to show in admin list view
    list_display = (
        'id',
        'Center_id',
        'Course_id',
        'Fiscal_year',
        'Participant_target',
        'Course_target',
        'Proposed_start_date',
        'Proposed_end_date',
        'Actual_start_date',
        'Actual_end_date',
    )

    # Enable search functionality
    search_fields = (
        'Fiscal_year',
        'Center_id__Center_name',
        'Course_id__Course_name',
    )

    # Add filters on the right-hand side
    list_filter = (
        'Fiscal_year',
        'Center_id',
        'Course_id',
    )

    # Pagination
    list_per_page = 25

    # Default ordering
    ordering = ('-id',)
