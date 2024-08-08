from django.urls import path
from . import views

urlpatterns = [
    path(
        "avaliacao/",
        views.AutorCreateListView.as_view(),
        name="avaliacao_create_list_view",
    ),
    path(
        "avaliacao/<int:pk>/",
        views.AutorRetrieveUpdateDestroyView.as_view(),
        name="avaliacao_detalhe_view",
    ),
]
