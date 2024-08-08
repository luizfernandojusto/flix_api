from django.db import models

from genero.models import Genero
from autor.models import Autor


class Filme(models.Model):
    titulo = models.CharField(max_length=500)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name="filme")
    data_lancamento = models.DateField(null=True, blank=True)
    autor = models.ManyToManyField(Autor, related_name="filme")
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
