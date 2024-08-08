from rest_framework import generics
from avaliacao.serializers import AvaliacaoSerializer
from rest_framework.permissions import IsAuthenticated

from avaliacao.models import Avaliacao
from app.permissions import PermissaoAcessoUtil


class AutorCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AutorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
