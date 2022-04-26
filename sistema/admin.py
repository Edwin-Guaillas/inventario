from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Almacen, Cuentas_cobrar

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    lis_display = ('nombre', 'descripcion')
    search_fields = ['nombre']


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'detalles', 'cantidad',
                    'precio', 'imagen', 'fk_categoria')
    search_fields = ['nombre', 'detalles']


class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'ciudad',
                    'direccion')
    search_fields = ['nombre', 'ciudad']


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion',
                    'descripcion', 'fecha_creacion', 'estado')
    search_fields = ['nombre', 'fecha_creacion', 'apellido']


class Cuentas_cobrarAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cedula', 'producto',
                    'precio', 'fecha_comprado')
    search_fields = ['cliente', 'cedula']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Cuentas_cobrar, Cuentas_cobrarAdmin)
