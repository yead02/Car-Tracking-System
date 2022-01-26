from django.db import models

# Create your models here.

class Tracking(models.Model):
    TrackingId = models.IntegerField(unique=True, auto_created=True)
    CarID = models.IntegerField()
    CurrentLocation = models.CharField(max_length=100)