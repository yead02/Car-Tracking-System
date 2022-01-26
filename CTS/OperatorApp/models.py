from django.db import models

# Create your models here.

class Operator(models.Model):
    OperatorId = models.IntegerField(unique=True, auto_created=True)
    OperatorName = models.CharField(max_length=100)
    OperatorCode = models.CharField(max_length=100)