from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg

from filme.models import Filme
from filme.serializers import FilmeSerializer, FilmeSerializerDetalhe
from avaliacao.models import Avaliacao
from app.permissions import PermissaoAcessoUtil


class AutorCreateListView(generics.ListCreateAPIView):

    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Filme.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FilmeSerializerDetalhe

        return FilmeSerializer


class AutorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Filme.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FilmeSerializerDetalhe

        return FilmeSerializer


class EstatísticaView(views.APIView):

    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Filme.objects.all()

    def get(self, request):

        qtd_filme = self.queryset.count()
        filme_por_genero = self.queryset.values("genero__nome").annotate(
            count=Count("id")
        )
        avaliacao = Avaliacao.objects.count()
        media_estrela = Avaliacao.objects.aggregate(avg_estrela=Avg("estrela"))[
            "avg_estrela"
        ]

        data = {
            "qtd_filme": qtd_filme,
            "filme_por_genero": filme_por_genero,
            "avaliacao": avaliacao,
            "media_estrela": round(media_estrela, 1) if media_estrela else 0,
        }

        return response.Response(
            data=data,
            status=status.HTTP_200_OK,
        )
