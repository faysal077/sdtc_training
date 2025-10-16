from django.db import models
from django.urls import reverse


class Budget(models.Model):
    center_id = models.IntegerField()
    name = models.CharField(max_length=255)
    echonomic_code = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    allocation = models.IntegerField()
    achivement = models.CharField(max_length=255, blank=True, null=True)
    requirement = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = "Budget"  # Maps to your existing table

    def __str__(self):
        return f"{self.name} ({self.echonomic_code})"

    def get_absolute_url(self):
        return reverse("edit", kwargs={"budget_id": self.id})

