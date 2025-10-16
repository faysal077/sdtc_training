from django.contrib import admin
from .models import PersonalInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_id', 'name', 'designation', 'office', 'contact_number', 'email')
    search_fields = ('name', 'designation', 'office', 'email')
    list_filter = ('designation', 'office')

