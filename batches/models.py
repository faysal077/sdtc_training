from django.db import models
from courses.models import Course
from centers.models import Center
from django.utils import timezone
class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    Center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    Fiscal_year = models.CharField(max_length=10, default="N/A")  # <- default added
    Participant_target = models.IntegerField()
    Course_target = models.IntegerField()
    Proposed_start_date = models.DateField(null=True, blank=True)
    Proposed_end_date = models.DateField(null=True, blank=True)
    Actual_start_date = models.DateField(null=True, blank=True)
    Actual_end_date = models.DateField(null=True, blank=True)


    class Meta:
        db_table = "Batch_table"

    def __str__(self):
        return f"{self.Course_id.Course_name} - Batch {self.id}"
