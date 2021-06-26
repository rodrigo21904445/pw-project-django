from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return f"{self.name} is {self.username}: {self.email}"


class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    duration = models.IntegerField()
    genre = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} uploaded {self.name}: {self.duration} ({self.genre})"

class Playlist(models.Model):
    name = models.ManyToManyField(Music, blank=True)
    user = ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=64)

    def __str__(self):
        return f"Playlist {self.name}: {self.user} -> {self.genre}"
    
class Contacto(models.Model):
    contacto_id = models.IntegerField()
    nome = models.CharField(max_length=64)
    apelido = models.CharField(max_length=64)
    telefone = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    dataNascimento = models.DateField()

    def __str__(self):
        return f"Contacto: {self.contacto_id}, {self.nome} {self.apelido} ({self.telefone}) com {self.email} nascido em {self.dataNascimento}"