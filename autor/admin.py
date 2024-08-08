from django.contrib import admin
from autor.models import Autor


@admin.register(Autor)
class Gerero(admin.ModelAdmin):
    list_display = ("id", "nome", "nacionalidade", "data_nascimento")
