from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return f"{self.name} is {self.username}: {self.email}"


class Music(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    duration = models.IntegerField()
    genre = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} uploaded {self.name}: {self.duration} ({self.genre})"

    

