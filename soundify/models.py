from django.db import models

# Create your models here.
class Music(models.Model):
    user = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    duration = models.IntegerField()
    genre = models.CharField(max_length=64)