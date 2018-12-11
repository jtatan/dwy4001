from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import ProLista_Listar, ProLista_Comprar, ProLista_Actualizador, Lista_Listar, Lista_Actualizador

app_name = 'compra'
urlpatterns = [
    path('listado/', ProLista_Listar.as_view(), name="compra_lista"),
    url(r'^(?P<pk>\d+)/$', ProLista_Comprar.as_view(), name="compra_comprar"),
    url(r'^actualizar/(?P<pk>\d+)/$', ProLista_Actualizador.as_view(), name="comprar_actualizar"),

    path('lista/listar/', Lista_Listar.as_view(), name="lista_listar"),
    url(r'^listado/(?P<pk>\d+)/$', ProLista_Listar.as_view(), name="compra_lista_id"),

    url(r'^lista/actualizar/(?P<pk>\d+)/$', Lista_Actualizador.as_view(), name="lista_actualizar"),



]