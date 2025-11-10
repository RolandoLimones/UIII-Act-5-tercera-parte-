from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Sucursal, Almacen
from django.urls import reverse
from django.utils import timezone

def inicio_autozone(request):
    # Página de inicio; puedes añadir más contexto si quieres
    return render(request, 'inicio.html')

def agregar_proveedor(request):
    if request.method == 'POST':
        # No validamos según tu instrucción
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_registro = request.POST.get('fecha_registro')  # formato YYYY-MM-DD
        dias_entrega = request.POST.get('dias_entrega')
        hora_entrega = request.POST.get('hora_entrega')

        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_registro=fecha_registro,
            dias_entrega=dias_entrega,
            hora_entrega=hora_entrega
        )
        return redirect('ver_proveedores')

    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.fecha_registro = request.POST.get('fecha_registro')
        proveedor.dias_entrega = request.POST.get('dias_entrega')
        proveedor.hora_entrega = request.POST.get('hora_entrega')
        proveedor.save()
        return redirect('ver_proveedores')
    # si no es POST, redirige a la página de edición
    return redirect('actualizar_proveedor', proveedor_id=proveedor.id)

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ============================================================
# AGREGAR SUCURSAL
# ============================================================
def agregar_sucursal(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        fecha_apertura = request.POST.get('fecha_apertura')
        horario = request.POST.get('horario')
        id_proveedor = request.POST.get('id_proveedor')
        
        proveedor = Proveedor.objects.get(id=id_proveedor)
        Sucursal.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            ciudad=ciudad,
            fecha_apertura=fecha_apertura,
            horario=horario,
            id_proveedor=proveedor
        )
        return redirect('ver_sucursal')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'sucursal/agregar_sucursal.html', {'proveedores': proveedores})

# ============================================================
# VER SUCURSALES
# ============================================================
def ver_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursal.html', {'sucursales': sucursales})

# ============================================================
# ACTUALIZAR SUCURSAL (FORMULARIO)
# ============================================================
def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal, 'proveedores': proveedores})

# ============================================================
# REALIZAR ACTUALIZACIÓN
# ============================================================
def realizar_actualizacion_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == "POST":
        sucursal.nombre = request.POST.get('nombre')
        sucursal.direccion = request.POST.get('direccion')
        sucursal.telefono = request.POST.get('telefono')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.fecha_apertura = request.POST.get('fecha_apertura')
        sucursal.horario = request.POST.get('horario')
        proveedor_id = request.POST.get('id_proveedor')
        sucursal.id_proveedor = Proveedor.objects.get(id=proveedor_id)
        sucursal.save()
        return redirect('ver_sucursal')

# ============================================================
# BORRAR SUCURSAL
# ============================================================
def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == "POST":
        sucursal.delete()
        return redirect('ver_sucursal')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# ============================================================
# AGREGAR ALMACÉN
# ============================================================
def agregar_almacen(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        capacidad_max = request.POST.get('capacidad_max')
        capacidad_disp = request.POST.get('capacidad_disp')
        telefono = request.POST.get('telefono')
        horario = request.POST.get('horario')
        id_sucursal = request.POST.get('id_sucursal')

        sucursal = Sucursal.objects.get(id=id_sucursal)
        Almacen.objects.create(
            id_sucursal=sucursal,
            nombre=nombre,
            direccion=direccion,
            capacidad_max=capacidad_max,
            capacidad_disp=capacidad_disp,
            telefono=telefono,
            horario=horario
        )
        return redirect('ver_almacen')

    sucursales = Sucursal.objects.all()
    return render(request, 'almacen/agregar_almacen.html', {'sucursales': sucursales})


# ============================================================
# VER ALMACENES
# ============================================================
def ver_almacen(request):
    almacenes = Almacen.objects.all()
    return render(request, 'almacen/ver_almacen.html', {'almacenes': almacenes})


# ============================================================
# ACTUALIZAR ALMACÉN (FORMULARIO)
# ============================================================
def actualizar_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    sucursales = Sucursal.objects.all()
    return render(request, 'almacen/actualizar_almacen.html', {
        'almacen': almacen,
        'sucursales': sucursales
    })


# ============================================================
# REALIZAR ACTUALIZACIÓN DE ALMACÉN
# ============================================================
def realizar_actualizacion_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    if request.method == "POST":
        almacen.nombre = request.POST.get('nombre')
        almacen.direccion = request.POST.get('direccion')
        almacen.capacidad_max = request.POST.get('capacidad_max')
        almacen.capacidad_disp = request.POST.get('capacidad_disp')
        almacen.telefono = request.POST.get('telefono')
        almacen.horario = request.POST.get('horario')
        sucursal_id = request.POST.get('id_sucursal')
        almacen.id_sucursal = Sucursal.objects.get(id=sucursal_id)
        almacen.save()
        return redirect('ver_almacen')


# ============================================================
# BORRAR ALMACÉN
# ============================================================
def borrar_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    if request.method == "POST":
        almacen.delete()
        return redirect('ver_almacen')
    return render(request, 'almacen/borrar_almacen.html', {'almacen': almacen})