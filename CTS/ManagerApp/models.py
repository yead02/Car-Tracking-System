from django.db import models

# Create your models here.

class Manager(models.Model):
    ManagerId = models.IntegerField(unique=True, auto_created=True)
    ManagerName = models.CharField(max_length=100)
    ManagerPassword = models.CharField(max_length=100)