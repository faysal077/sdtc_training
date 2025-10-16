from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_id', 'name', 'echonomic_code', 'allocation', 'achivement', 'requirement')
    search_fields = ('name', 'echonomic_code', 'description')
    list_filter = ('center_id',)
    ordering = ('id',)
