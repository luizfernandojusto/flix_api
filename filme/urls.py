from django.urls import path
from . import views

urlpatterns = [
    path('filme/', views.AutorCreateListView.as_view(), name='filme_create_list_view'),
    path('filme/<int:pk>/', views.AutorRetrieveUpdateDestroyView.as_view(), name='filme_detalhe_view'),
    path('filme/estatistica/', views.EstatísticaView.as_view(), name='filme_estatistica_view'),
]
