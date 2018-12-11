from django import forms
from apps.compra.models import ProLista, Lista


class ProLista_Formulario(forms.ModelForm):
    class Meta:
        model = ProLista

        fields = [
            'producto',
            'cantidad',
            'costo_presupuestado',
            'tienda',
            'lista',

        ]
        labels = {
            'producto': 'Producto',
            'cantidad': 'Cantidad',
            'costo_presupuestado': 'Costo Presupuestado',
            'tienda': 'Tienda',
            'lista': 'Lista',
        }
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'costo_presupuestado': forms.NumberInput(attrs={'class': 'form-control'}),
            'tienda': forms.Select(attrs={'class': 'form-control'}),
            'lista': forms.Select(attrs={'class': 'form-control'}),
        }

class ProLista_Compra(forms.ModelForm):
    class Meta:
        model = ProLista

        fields = [
            'costo_real',
            'comprado'
        ]
        labels = {
            'costo_real': 'Costo Real',
            'comprado': 'Comprar'
        }
        widgets = {

            'costo_real': forms.NumberInput(attrs={'class': 'form-control'}),
            'comprado': forms.CheckboxInput(attrs={'class': 'form-control'})

        }

class Lista_Formulario(forms.ModelForm):
    class Meta:
        model = Lista

        fields = [
            'nombre',
            'finalizada'
        ]
        labels = {
            'nombre': 'Nombre',
            'finalizada': 'Finalizado'
        }
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'finalizada': forms.CheckboxInput(attrs={'class': 'form-control'})

        }