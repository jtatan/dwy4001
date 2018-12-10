from django.contrib import admin
from .models import ProLista, Lista, Compra

# Register your models here.

admin.site.register(ProLista),
admin.site.register(Lista),
admin.site.register(Compra)