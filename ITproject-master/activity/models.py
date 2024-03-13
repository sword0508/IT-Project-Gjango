from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import User

class Activity(models.Model):
    user = models.ForeignKey(to=User, related_name='activity', on_delete=models.SET,
                             blank=True, null=True)

    date = models.CharField(max_length=100, default="03/20/2024")

    time = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=100, default=" ")

    peo_num = models.PositiveIntegerField(default=1)
    coasts = models.PositiveIntegerField(default=1)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

