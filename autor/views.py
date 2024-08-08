from rest_framework import generics
from autor.serializers import AutorSerializer
from rest_framework.permissions import IsAuthenticated

from autor.models import Autor
from app.permissions import PermissaoAcessoUtil


class AutorCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        PermissaoAcessoUtil,
    )
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
