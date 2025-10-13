from django.db import models
from courses.models import Course
from centers.models import Center

class Batch(models.Model):
    id = models.AutoField(primary_key=True)
    Center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    Fiscal_year = models.DateTimeField()
    Participant_target = models.IntegerField()
    Course_target = models.IntegerField()
    Proposed_start_date = models.DateTimeField()
    Proposed_end_date = models.DateTimeField()
    Actual_start_date = models.DateTimeField(null=True, blank=True)
    Actual_end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "Batch_table"

    def __str__(self):
        return f"Batch {self.id} ({self.Course.course_title})"
