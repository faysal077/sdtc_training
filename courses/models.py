from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    Center_id = models.IntegerField()
    Course_name = models.CharField(max_length=255)
    Course_duration = models.CharField(max_length=255)
    Batch_number = models.IntegerField()

    class Meta:
        db_table = "Course_table"  # Explicitly link to your existing table

    def __str__(self):
        return self.Course_name
