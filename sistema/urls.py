from rest_framework import routers
from .viewset import *

routers = routers.SimpleRouter()
routers.register('', CategoriaViewSet)
routers.register('api/producto', ProductoViewSet)
routers.register('api/almacen', AlmacenViewSet)
routers.register('api/proveedor', ProveedorViewSet)
routers.register('api/cuentas_cobrar', Cuentas_cobrarViewSet)

urlpatterns = routers.urls
