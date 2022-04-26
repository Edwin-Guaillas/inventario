from rest_framework import viewsets
from .serializer import *
from .models import *


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class Cuentas_cobrarViewSet(viewsets.ModelViewSet):
    queryset = Cuentas_cobrar.objects.all()
    serializer_class = CategoriaSerializer
