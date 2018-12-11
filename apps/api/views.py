from django.shortcuts import render
from rest_framework import viewsets
from apps.tienda.models import Tienda
from apps.producto.models import Producto
from apps.api.serializer import ProductoSerializer, TiendaSerializer

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
