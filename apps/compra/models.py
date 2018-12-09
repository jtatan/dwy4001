from django.db import models
from apps.producto.models import Producto
from apps.tienda.models import Tienda


# Create your models here.

class ProLista(models.Model):
    nombre = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    costo_presupuestado = models.IntegerField()
    cantidad = models.IntegerField()
    costo_real = models.IntegerField()
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)


class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    lista_productos = models.ForeignKey('ProLista', null=True, blank=True, on_delete=models.CASCADE)
    totalagregados = models.IntegerField()
    totalpresupuestado = models.IntegerField()
    finalizada = models.BooleanField(default=False)


class Compra(models.Model):
    lista = models.ForeignKey('Lista', null=True, blank=True)
    totalreal = models.IntegerField()
    totalfinal = models.IntegerField()
