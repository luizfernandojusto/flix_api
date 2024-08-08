from django.contrib import admin
from genero.models import Genero


@admin.register(Genero)
class Gerero(admin.ModelAdmin):
    list_display = ("id", "nome")
