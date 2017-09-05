from django.contrib import admin
from .models import Album


class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Album, AlbumModelAdmin)
