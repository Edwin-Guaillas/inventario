"""inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sistema.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('sistema.urls')),
    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    path('logout/', logout_view, name="vista_logout"),
    #======================URLS CON VISTAS BASADAS EN CLASES==============================#
    # ----------------------- Categoria ------------------------------------------
    path('listado_categorias/', login_required(ListadoCategoria.as_view()),
         name="listado_categorias"),
    path('registrar_categoria/', login_required(CrearCategoria.as_view()),
         name="registrar_categoria"),
    path('editar_categoria/<int:pk>/',
         login_required(ActualizarCategoria.as_view()), name="editar_categoria"),
    path('eliminar_Categoria/<int:pk>/',
         login_required(EliminarCategoria.as_view()), name="eliminar_categoria"),
    # -----------------------productos--------------------------------------------------------
    path('gestion_producto/', login_required(ListadoProducto.as_view()),
         name="gestion_productos"),
    path('crear_producto/', login_required(CrearProducto.as_view()),
         name="crear_productos"),
    path('modal_compra/<int:pk>/',
         login_required(VenderProducto.as_view()), name="modal_compra"),
    # ----------------------- Almacen --------------------------------
    path('listado_almacenes/', login_required(ListadoAlmacen.as_view()),
         name="listado_almacenes"),
    path('registrar_almacen/', login_required(CrearAlmacen.as_view()),
         name="registrar_almacen"),
    path('editar_almacen/<int:pk>/',
         login_required(ActualizarAlmacen.as_view()), name="editar_Almacen"),
    path('eliminar_Almacen/<int:pk>/',
         login_required(EliminarAlmacen.as_view()), name="eliminar_Almacen"),
    # -----------------------proveedor------------------------
    path('lista_proveedor/', login_required(ListadoProveedor.as_view()),
         name="listar_proveedor"),
    path('crear_proveedor/', login_required(CrearProveedor.as_view()),
         name="crear_proveedor"),
    path('editar_proveedor/<int:pk>/',
         login_required(ActualizarProveedor.as_view()), name="editar_proveedor"),
    path('eliminar_proveedor/<int:pk>/',
         login_required(EliminarProveedor.as_view()), name="eliminar_proveedor"),

    # -----------------------cuentas------------------------------------------
    path('registro_cuentas/', login_required(ListadoCuentas.as_view()),
         name="registro_cuentas"),
    path('registar_cuenta/', login_required(CrearCuentas.as_view()),
         name="registrar_cuentas"),
    path('editar_cuenta/<int:pk>/',
         login_required(ActualizarCuenta.as_view()), name="editar_cuentas"),
    path('eliminar_cuentas/<int:pk>/',
         login_required(EliminarCuenta.as_view()), name="eliminar_cuentas"),

]
admin.site.site_header = 'SISTEMA DE GESTION MARKLENS MOTORS'
