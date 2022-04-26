from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

#Lubricantes, llantas, repuestos, neumaticos


class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


def url_producto(self, filename):
    ruta = "static/img/Productos/%s/%s" % (self.nombre, str(filename))
    return ruta


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    detalles = models.TextField()
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    imagen = models.ImageField(upload_to=url_producto)
    fk_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, default="")

    def imagen_producto(self):
        return mark_safe('<a href="/%s" target="_blank"><img src="/%s" higth="50px" width="50px" ></a>' % (self.imagen, self.imagen))
    imagen_producto.allow_tags = True

    def __str__(self):
        return self.nombre


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=140)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre


class Proveedor (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=True)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


class Cuentas_cobrar(models.Model):
    cliente = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=4)
    fecha_comprado = models.DateField('Fecha de Compra', auto_now=True)

    def __str__(self):
        return self.cliente
