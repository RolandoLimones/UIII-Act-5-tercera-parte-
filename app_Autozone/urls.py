from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_autozone, name='inicio_autozone'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/editar/<int:proveedor_id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/editar/guardar/<int:proveedor_id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
    path('agregar_sucursal/', views.agregar_sucursal, name='agregar_sucursal'),
    path('ver_sucursal/', views.ver_sucursal, name='ver_sucursal'),
    path('actualizar_sucursal/<int:id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('realizar_actualizacion_sucursal/<int:id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('borrar_sucursal/<int:id>/', views.borrar_sucursal, name='borrar_sucursal'),
    path('agregar_almacen/', views.agregar_almacen, name='agregar_almacen'),
    path('ver_almacen/', views.ver_almacen, name='ver_almacen'),
    path('actualizar_almacen/<int:id>/', views.actualizar_almacen, name='actualizar_almacen'),
    path('realizar_actualizacion_almacen/<int:id>/', views.realizar_actualizacion_almacen, name='realizar_actualizacion_almacen'),
    path('borrar_almacen/<int:id>/', views.borrar_almacen, name='borrar_almacen'),
]