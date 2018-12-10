from django.db import models
from apps.producto.models import Producto
from apps.tienda.models import Tienda


# Create your models here.

class ProLista(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    costo_presupuestado = models.IntegerField(null=True, blank=True)
    total_presupuestado = models.IntegerField(null=True, blank=True)
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    costo_real = models.IntegerField(null=True, blank=True)
    total_real = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.producto)


class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    lista_productos = models.ForeignKey(ProLista, null=True, blank=True, on_delete=models.CASCADE)
    totalagregados = models.IntegerField()
    totalpresupuestado = models.IntegerField()
    finalizada = models.BooleanField(default=False)


class Compra(models.Model):
    lista = models.ForeignKey('Lista', null=True, blank=True, on_delete=models.CASCADE)
    totalreal = models.IntegerField()
    totalfinal = models.IntegerField()
