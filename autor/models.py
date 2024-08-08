from django.db import models


NACIONALIDADE_CHOICES = (
    ("USA", "Estado Unidos"),
    ("BRASIL", "Brasil"),
)


class Autor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(
        max_length=100, choices=NACIONALIDADE_CHOICES, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.nome
