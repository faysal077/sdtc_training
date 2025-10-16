from django.db import models
from django.urls import reverse


class PersonalInfo(models.Model):
    center_id = models.IntegerField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField()


    class Meta:
        db_table = "Personal_info"  # Maps to your existing table

    def __str__(self):
        return f"{self.name} - {self.designation}"

    def get_absolute_url(self):
        return reverse("edit", kwargs={"person_id": self.id})
