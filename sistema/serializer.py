from rest_framework import serializers
from .models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class Cuentas_cobrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas_cobrar
        fields = '__all__'
