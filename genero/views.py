from rest_framework import generics
from genero.serializers import GeneroSerializer
from rest_framework.permissions import IsAuthenticated


from genero.models import Genero
from app.permissions import PermissaoAcessoUtil


class GeneroCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GeneroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
