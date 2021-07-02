from django.contrib import admin

from .models import Music, User, Playlist, Contacto, Quizz, Comentario

# Register your models here.
admin.site.register(Music)
admin.site.register(User)
admin.site.register(Playlist)
admin.site.register(Contacto)
admin.site.register(Quizz)
admin.site.register(Comentario)