# centers/models.py
from django.db import models

class Center(models.Model):
    Center_name = models.CharField(max_length=255)
    Establishment_year = models.DateTimeField()
    District = models.CharField(max_length=255)
    RD_office = models.CharField(max_length=255)
    Officer_in_charge = models.CharField(max_length=255)

    class Meta:
        db_table = "Center"

    def __str__(self):
        return self.Center_name
