from django.urls import path
from . import views

urlpatterns = [
    path('genero/', views.GeneroCreateListView.as_view(), name='genero_create_list_view'),
    path('genero/<int:pk>/', views.GeneroRetrieveUpdateDestroyView.as_view(), name='genero_detalhe_view'),
]
