from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .models import ProLista, Lista
from django.urls import reverse_lazy

from apps.compra.formularios import ProLista_Formulario, ProLista_Compra, Lista_Formulario

# Create your views here.
#LISTA

class Lista_Listar(ListView):
    template_name = 'compra/lista_listar.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Lista.objects.all()

class Lista_Actualizador(UpdateView):
    model = Lista
    form_class = Lista_Formulario
    template_name = 'compra/lista_crear.html'
    success_url = reverse_lazy('compra:lista_listar')

class Lista_Crear(CreateView):
    model = Lista
    form_class = Lista_Formulario
    template_name = 'compra/lista_crear.html'
    success_url = reverse_lazy('compra:compra_lista')

#PROLISTA
class ProLista_Listar(ListView):
    template_name = 'compra/lista_productos_listar.html'
    context_object_name = 'lista_producto'

    def get_queryset(self):
        return ProLista.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        productos = context['object_list']
        total = 0
        for producto in productos:
            if producto.comprado == True:
                total += producto.cantidad * producto.costo_real
        context['total_comprado'] = total


        total_final = 0
        for producto in productos:
            total_final += producto.cantidad * producto.costo_presupuestado
        context['total_presupuestado'] = total_final

        return context

class ProLista_Actualizador(UpdateView):
    model = ProLista
    form_class = ProLista_Formulario
    template_name = 'compra/lista_productos_crear.html'
    success_url = reverse_lazy('compra:compra_lista')

class ProLista_Comprar(UpdateView):
    model = ProLista
    form_class = ProLista_Compra
    template_name = 'compra/lista_productos_comprar.html'
    success_url = reverse_lazy('compra:compra_lista')

class ProLista_Crear(CreateView):
    model = ProLista
    form_class = ProLista_Formulario
    template_name = 'compra/lista_productos_comprar.html'
    success_url = reverse_lazy('compra:compra_lista')
