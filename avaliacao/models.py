from django.db import models
from filme.models import Filme

from django.core.validators import MinValueValidator, MaxValueValidator


class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT, related_name="avaliacao")
    estrela = models.IntegerField(
        validators=[
            MinValueValidator(0, "Não pode ser menor que zero!"),
            MaxValueValidator(5, "Não pode ser maior que zero!"),
        ]
    )
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.filme.titulo
