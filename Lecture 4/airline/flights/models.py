from django.db import models

# Create your models here.
class Flight(models.model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()