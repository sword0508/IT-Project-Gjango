from django.db import models

# Create your models here.
class Activity(models.Model):
    activity_id = models.IntegerField()
    activity_name = models.CharField(max_length=128)
    start_date = models.DateField()
    duration = models.IntegerField()
    vacancy = models.IntegerField()
    type = models.CharField(max_length=128)
    theme = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    resources = models.CharField(max_length=128)

class Destination(models.Model):
    destination_id = models.IntegerField()
    destination_name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)