# miaplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),  # Ruta URL para agregar una categoría
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  # Ruta URL para agregar un producto
    path('buscar-productos/', views.buscar_productos, name='buscar_productos'),  # Ruta URL para buscar productos
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente-agregado/', views.cliente_agregado, name='cliente_agregado'),
]
