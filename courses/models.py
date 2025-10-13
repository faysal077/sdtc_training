from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    Center_id = models.IntegerField()
    Course_name = models.CharField(max_length=255)
    Course_duration = models.CharField(max_length=255)
    Batch_number = models.IntegerField()



    def __str__(self):
        return self.Course_name
class Batch(models.Model):
    center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_no = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = "Course_table"  # Explicitly link to your existing table

    def __str__(self):
        return f"{self.course_id.course_name} - Batch {self.batch_no}"  # ✅ CORRECT