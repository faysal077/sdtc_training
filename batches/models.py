from django.db import models

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    Center_id = models.IntegerField()
    Course_id = models.IntegerField()
    Fiscal_year = models.DateTimeField()
    Participant_target = models.IntegerField()
    Course_target = models.IntegerField()
    Proposed_start_date = models.DateTimeField()
    Proposed_end_date = models.DateTimeField()
    Actual_start_date = models.DateTimeField(null=True, blank=True)
    Actual_end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "Batch_table"  # Link to existing table

    def __str__(self):
        return f"Batch {self.id} (Course: {self.Course_id})"
