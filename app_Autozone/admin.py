from django.contrib import admin
from .models import Proveedor, Sucursal, Almacen

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'email')

# Registramos Sucursal y Almacen (aunque por ahora no trabajaremos con ellos)
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'id_proveedor')
    search_fields = ('nombre', 'ciudad')

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_sucursal', 'capacidad_disp')