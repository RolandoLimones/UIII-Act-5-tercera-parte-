from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    fecha_registro = models.DateField()
    dias_entrega = models.CharField(max_length=150)
    hora_entrega = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    fecha_apertura = models.DateField()
    horario = models.CharField(max_length=100)
    id_proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE,
        related_name='sucursales',
        verbose_name='Proveedor'
    )
    
    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"


class Almacen(models.Model):
    id_sucursal = models.ForeignKey(
        Sucursal, 
        on_delete=models.CASCADE,
        related_name='almacenes',
        verbose_name='Sucursal'
    )
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad_max = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad_disp = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'
    
    def __str__(self):
        return f"{self.nombre} - {self.id_sucursal.nombre}"