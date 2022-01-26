from django.db import models

# Create your models here.

class City(models.Model):
    CityId = models.IntegerField(unique=True, auto_created=True)
    CityName = models.CharField(max_length=100)
    CarID = models.IntegerField()
    File = models.FileField()