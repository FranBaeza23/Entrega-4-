from django import forms
from django.forms.models import ModelChoiceField
from django.forms import ModelForm,widgets 
from .models import datos

class datosForm(ModelForm):

    class Meta:
        model = datos
        fields = ['rutcola', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'contrasena']

        labels={
            'rutcola': 'rut colaborador: ',
            'nombre': 'nombre: ',
            'telefono': 'telefono: ',
            'direccion': 'direccion: ',
            'email': 'email: ',
            'pais': 'pais: ',
            'contrasena': 'contrasena: ',
        
        }
        widgets={
            'rutcola': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rutcola', 
                    'name': 'rut',
                    'placeholder': 'Digite rut'
                }
            ),
            'nombre ': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre', 
                    'name': 'nombre',
                    'placeholder': 'Digite nombre'

                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                    'name': 'telefono', 
                    'placeholder': 'Digite telefono'

                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'name': 'direccion', 
                    'placeholder': 'Digite direccion'

                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email', 
                    'name': 'email',
                    'placeholder': 'Digite email'

                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'pais',
                    'name': 'pais', 
                    'placeholder': 'Digite pais'

                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contrasena',
                    'name': 'contrasena', 
                    'placeholder': 'Digite contrasena'

                }
            )
        }