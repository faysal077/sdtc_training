from django.contrib import admin
from .models import Participant, JobHistory


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'gender',
        'center_id',
        'course_id',
        'batch_id',
        'date_of_birth',
        'job_status',
    )
    list_filter = ('gender', 'job_status', 'center_id', 'course_id', 'batch_id')
    search_fields = ('name', 'father_name', 'nid', 'birth_reg', 'email', 'contact_number')
    list_per_page = 20


@admin.register(JobHistory)
class JobHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'participant',
        'company_name',
        'designation',
        'start_date',
        'end_date',
        'currently_employed',
    )
    list_filter = ('currently_employed',)
    search_fields = ('company_name', 'designation', 'participant__name')
    list_per_page = 20
