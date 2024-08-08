from rest_framework import serializers
from filme.models import Filme
from django.db.models import Avg

from genero.serializers import GeneroSerializer
from autor.serializers import AutorSerializer


class FilmeSerializer(serializers.ModelSerializer):

    # read_only=True apenas dados de leitura, ou seja nao deve aparecer quando for cadastrar

    estrela_media = serializers.SerializerMethodField(read_only=True)
    qtd_avaliacao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = "__all__"

    # get + nome campo
    def get_estrela_media(self, obj):

        media = obj.avaliacao.aggregate(Avg("estrela"))["estrela__avg"]
        return round(media, 1) if media is not None else 0

    def get_qtd_avaliacao(self, obj):

        qtd = obj.avaliacao.all().count()
        return qtd if qtd is not None else 0

    #  validate + nome campo
    def validate_data_lancamento(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1990."
            )
        return value

    def validate_resumo(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                f"O resumo não deve ser maior que 200 caracteres. Contem {len(value)} caracteres."
            )
        return value


class FilmeSerializerDetalhe(serializers.ModelSerializer):

    genero = GeneroSerializer()
    autor = AutorSerializer(many=True)  # muitos generos precisa usar many=True

    estrela_media = serializers.SerializerMethodField(read_only=True)
    qtd_avaliacao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = [
            "id",
            "estrela_media",
            "qtd_avaliacao",
            "titulo",
            "data_lancamento",
            "resumo",
            "genero",
            "autor",
        ]

    def get_estrela_media(self, obj):

        media = obj.avaliacao.aggregate(Avg("estrela"))["estrela__avg"]
        return round(media, 1) if media is not None else 0

    def get_qtd_avaliacao(self, obj):

        qtd = obj.avaliacao.all().count()
        return qtd if qtd is not None else 0
