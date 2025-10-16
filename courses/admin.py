from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # These fields will appear as columns in the admin list view
    list_display = ('id', 'Center_id', 'Course_name', 'Course_duration', 'Batch_number')

    # Optional: Allow searching by course name or duration
    search_fields = ('Course_name', 'Course_duration')

    # Optional: Add filters in sidebar
    list_filter = ('Center_id', 'Course_duration')
