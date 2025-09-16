from django.db import models
from datetime import date

# Create your models here.
class Attendance(models.Model):
    Staffid=models.CharField(max_length=5)
    Date=models.DateField(default=date.today)
    punch_in_time = models.TimeField(null=True,blank=True)
    punch_out_time=models.TimeField(null=True,blank=True)
    

