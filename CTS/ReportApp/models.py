from django.db import models

# Create your models here.

class Report(models.Model):
    ReportId = models.IntegerField(unique=True, auto_created=True)
    CarID = models.IntegerField()
    DateTime = models.DateTimeField(auto_now_add=True)
    ReportDetails = models.CharField(max_length=100)