from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("autenticacao/token/", TokenObtainPairView.as_view(), name="token_obtem_pair"),
    path("autenticacao/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("autenticacao/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
