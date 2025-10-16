from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'center_id', 'name', 'category', 'condition', 'quantity')
    search_fields = ('name', 'category', 'condition')
    list_filter = ('category', 'condition')
    ordering = ('id',)

    def get_queryset(self, request):
        """
        Admins see all data. Normal users can be restricted if needed.
        """
        qs = super().get_queryset(request)
        # You can add filtering here if you want non-admin users to see only their center.
        return qs
