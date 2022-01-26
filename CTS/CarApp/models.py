from django.db import models

# Create your models here.

class Car(models.Model):
    CarId = models.IntegerField(unique=True, auto_created=True)
    CarName = models.CharField(max_length=100)
    OperatorId = models.IntegerField()