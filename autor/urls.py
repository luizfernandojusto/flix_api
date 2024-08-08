from django.urls import path
from . import views

urlpatterns = [
    path("autor/", views.AutorCreateListView.as_view(), name="autor_create_list_view"),
    path(
        "autor/<int:pk>/",
        views.AutorRetrieveUpdateDestroyView.as_view(),
        name="autor_detalhe_view",
    ),
]
