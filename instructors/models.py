from django.db import models
from django.urls import reverse


class Instructor(models.Model):
    center_id = models.IntegerField()
    type = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()


    def __str__(self):
        return f"{self.designation} ({self.type})"

    def get_absolute_url(self):
        return reverse("edit", kwargs={"instructor_id": self.id})


# Create your models here.
