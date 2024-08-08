from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("autenticacao.urls")),
    path("api/v1/", include("genero.urls")),
    path("api/v1/", include("autor.urls")),
    path("api/v1/", include("filme.urls")),
    path("api/v1/", include("avaliacao.urls")),
]
