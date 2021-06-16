from django.contrib import admin

from .models import Music, User, Playlist

# Register your models here.
admin.site.register(Music)
admin.site.register(User)
admin.site.register(Playlist)