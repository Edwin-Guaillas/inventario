from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Proveedor, Producto, Cuentas_cobrar, Categoria, Almacen


class LoginForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password']


class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre del Categoria',
            'apellido': 'Apellidos del Categoria',
            'direccion': 'Direccion del Categoria',
            'descripcion': 'Ingrese una decsripcion',
        }
        Widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'id': 'nombre',
                }
            ),

            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'id': 'descripcion',
                }
            ),
        }


class ProductosForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'detalles', 'cantidad',
                  'precio', 'imagen', 'fk_categoria']
        labels = {
            'nombre': 'Nombre del producto',
            'detalles': 'Ingrese los detalles del producto',
            'cantidad': 'Ingrese la cantidad de productos',
            'precio': 'Ingrese el precio por unidad',
            'imagen': 'Seleccione la imagen del producto',
            'fk_categoria': 'Categoria al que pertenece el producto',
        }
        Widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'id': 'nombre',
                }
            ),
            'detalles': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese algunos detalles del producto',
                    'id': 'detalles',
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad del producto',
                    'id': 'cantidad',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto por unidad',
                    'id': 'precio',
                }
            ),
            'imagen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione una imagen',
                    'id': 'imagen_producto',
                }
            ),
            'fk_categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione una categoria al que pertenece',
                    'id': 'fk_categoria',
                }
            ),

        }


class AlmacenForms(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['nombre', 'telefono', 'email', 'ciudad',
                  'direccion', 'productos']
        labels = {
            'nombre': 'Nobre del almacen',
            'telefono': 'Telefono del almacen',
            'email': 'Correo del almacen',
            'ciudad': 'Ciudad donde se ubica el almacen',
            'direccion': 'direccion del almacen',
            'productos': 'Porducto qu ofrece',
        }
        Widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Nombre del almacen',
                    'id': 'nombre',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el numero del telefono del almacen',
                    'id': 'telefono',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del almacen',
                    'id': 'email',
                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la ciudad donde se ubica el almacen',
                    'id': 'ciudad',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion del almacen',
                    'id': 'direccion',
                }
            ),
            'distribuidor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione el distribuidor del almacen',
                    'id': 'distribuidor',
                }
            ),
            'productos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccion el producto que distribuye',
                    'id': 'productos',
                }
            ),


        }


class ProveedorForms(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'direccion',
                  'descripcion']
        labels = {
            'nombre': 'Nombre del Proveedor',
            'apellido': 'Apellidos del Proveedor',
            'direccion': 'Direccion del Proveedor',
            'descripcion': 'Ingrese una decsripcion',
        }
        Widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'id': 'nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos',
                    'id': 'apellido',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion',
                    'id': 'direccion',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'id': 'descripcion',
                }
            ),
        }


class CuentasForms(forms.ModelForm):
    class Meta:
        model = Cuentas_cobrar
        fields = ['cliente', 'cedula', 'producto', 'precio']
        labels = {
            'cliente': 'Nobre del cliente',
            'cedula': 'Ingrese la cedula del cliente',
            'producto': 'Ingrese el producto',
            'precio': 'Ingrese el valor por cobrar',
        }
        Widgets = {
            'cliente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Nombre del cliente',
                    'id': 'cliente',
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cedula del cliente',
                    'id': 'cedula',
                }
            ),
            'producto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto',
                    'id': 'producto',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto por pagar',
                    'id': 'precio',
                }
            ),


        }
