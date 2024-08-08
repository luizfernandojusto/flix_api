from django.contrib import admin
from avaliacao.models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "filme", "estrela", "comentario")
