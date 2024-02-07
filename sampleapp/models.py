from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(blank=False,primary_key=True)
    sname = models.CharField(blank=False,max_length=50)

    class Meta:
        db_table = "student_table"
