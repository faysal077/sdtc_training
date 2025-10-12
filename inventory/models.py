from django.db import models
from django.urls import reverse


class Inventory(models.Model):
    center_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "Inventory"  # Use your existing table

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_absolute_url(self):
        return reverse("edit", kwargs={"item_id": self.id})
