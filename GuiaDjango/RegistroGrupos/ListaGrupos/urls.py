from django.urls import path
from ListaGrupos import views


urlpatterns = [
    path('registro/', views.registro),
    path('listado/', views.listado),
]