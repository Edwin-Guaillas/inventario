from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import *


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/inicio/')
        else:
            form = LoginForm()
            ctx = {'form': form}
            return render(request, 'login.html', ctx)


# @login_required(login_url='/login/')
def inicio_view(request):
    productos = Producto.objects.all()
    ctx = {'productos': productos}
    return render(request, 'plantilla/gestion_productos.html', ctx)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#=============================VISTAS BASADAS EN CLASES=====================#
# ----------------- Categoria ----------------------------------------------------


class ListadoCategoria(ListView):
    model = Categoria
    template_name = 'plantilla/listado_categorias.html'
    queryset = Categoria.objects.filter()
    context_object_name = 'categorias'


class CrearCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForms
    template_name = 'plantilla/registrar_categoria.html'
    success_url = reverse_lazy('listado_categorias')


class ActualizarCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForms
    template_name = 'plantilla/editar_categoria.html'
    success_url = reverse_lazy('listado_categorias')


class EliminarCategoria(DeleteView):
    model = Categoria
    form_class = CategoriaForms
    template_name = 'plantilla/eliminar_categoria.html'
    success_url = reverse_lazy('listado_categorias')

# -----------------Porductos--------------------------------


class ListadoProducto(ListView):
    model = Producto
    template_name = 'plantilla/gestion_productos.html'
    queryset = Producto.objects.filter()
    context_object_name = 'productos'


class CrearProducto(CreateView):
    model = Producto
    form_class = ProductosForms
    template_name = 'plantilla/crear_productos.html'
    success_url = reverse_lazy('gestion_productos')


class VenderProducto(DeleteView):
    model = Producto
    form_class = ProductosForms
    template_name = 'plantilla/modal_compra.html'
    success_url = reverse_lazy('gestion_productos')

# ____-------------------Almacen--------------


class ListadoAlmacen(ListView):
    model = Almacen
    template_name = 'plantilla/listado_almacenes.html'
    queryset = Almacen.objects.filter()
    context_object_name = 'almacenes'


class CrearAlmacen(CreateView):
    model = Almacen
    form_class = AlmacenForms
    template_name = 'plantilla/registrar_almacen.html'
    success_url = reverse_lazy('listado_almacenes')


class ActualizarAlmacen(UpdateView):
    model = Almacen
    form_class = AlmacenForms
    template_name = 'plantilla/editar_Almacen.html'
    success_url = reverse_lazy('listado_almacenes')


class EliminarAlmacen(DeleteView):
    model = Almacen
    form_class = AlmacenForms
    template_name = 'plantilla/eliminar_Almacen.html'
    success_url = reverse_lazy('listado_almacenes')

# -----------------------proveedor----------------------------------------


class ListadoProveedor(ListView):
    model = Proveedor
    template_name = 'plantilla/listar_proveedor.html'
    queryset = Proveedor.objects.filter(estado=True)
    context_object_name = 'proveedores'


class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForms
    template_name = 'plantilla/crear_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')


class ActualizarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForms
    template_name = 'plantilla/editar_proveedor.html'
    success_url = reverse_lazy('listar_proveedor')


class EliminarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForms
    template_name = 'plantilla/proveedor_confirm_delete.html'

    def post(self, request, pk, *args, **kwargs):
        object = Proveedor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('listar_proveedor')


# -----------------------Cuentas---------------------------------


class ListadoCuentas(ListView):
    model = Cuentas_cobrar
    template_name = 'plantilla/registro_cuentas.html'
    queryset = Cuentas_cobrar.objects.filter()
    context_object_name = 'cuentas'


class CrearCuentas(CreateView):
    model = Cuentas_cobrar
    form_class = CuentasForms
    template_name = 'plantilla/registrar_cuentas.html'
    success_url = reverse_lazy('registro_cuentas')


class ActualizarCuenta(UpdateView):
    model = Cuentas_cobrar
    form_class = CuentasForms
    template_name = 'plantilla/editar_cuentas.html'
    success_url = reverse_lazy('registro_cuentas')


class EliminarCuenta(DeleteView):
    model = Cuentas_cobrar
    form_class = CuentasForms
    template_name = 'plantilla/eliminar_cuenta_pendiente.html'
    success_url = reverse_lazy('registro_cuentas')
