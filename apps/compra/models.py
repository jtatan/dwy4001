from django.db import models
from apps.producto.models import Producto
from apps.tienda.models import Tienda


# Create your models here.

class ProLista(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    costo_presupuestado = models.PositiveIntegerField(null=True, blank=True)
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    costo_real = models.PositiveIntegerField(null=True)
    lista = models.ForeignKey('Lista', default='lista', null=False, blank=False, on_delete=models.CASCADE)
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.lista)


class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nombre)


class Compra(models.Model):
    lista = models.ForeignKey('Lista', null=True, blank=True, on_delete=models.CASCADE)
    total_agregados = models.IntegerField(null=True, blank=True)
    total_presupuestado = models.IntegerField(null=True, blank=True)
    total_real = models.IntegerField(null=True, blank=True)
    total_final = models.IntegerField(null=True, blank=True)