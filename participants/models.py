from django.db import models
from django.urls import reverse
from batches.models import Batch
from courses.models import Course
from centers.models import Center


class Participant(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nid = models.CharField(max_length=20, blank=True, null=True)
    birth_reg = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    educational_qualification = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    job_status = models.CharField(max_length=255, default="Unemployed")

    class Meta:
        db_table = "Participant_table"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("participants:participant_detail", kwargs={"pk": self.pk})


class JobHistory(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="job_histories")
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_employed = models.BooleanField(default=False)

    class Meta:
        db_table = "JobHistory_table"

    def __str__(self):
        return f"{self.company_name} - {self.designation}"
