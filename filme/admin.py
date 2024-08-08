from django.contrib import admin
from filme.models import Filme


@admin.register(Filme)
class Gerero(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "genero",
        "data_lancamento",
        "resumo",
    )

    search_fields = ("titulo", "genero")
