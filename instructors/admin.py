from django.contrib import admin
from .models import Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'center_id',
        'type',
        'designation',
        'contact_number',
        'email',
        'education',
        'contract_start_date',
        'contract_end_date',
    )

    search_fields = ('designation', 'type', 'email')
    list_filter = ('type', 'center_id')
    ordering = ('center_id',)
