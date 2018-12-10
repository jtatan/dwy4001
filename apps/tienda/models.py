from django.db import models

# Create your models here.



class Tienda(models.Model):
    nombre = models.CharField(max_length=50)
    pendiente = models.BooleanField(default=True)


