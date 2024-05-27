from django.shortcuts import render, redirect

from historial.Historial import Historial
from crud.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {'productos':productos})

def h_agregar_producto(request, producto_id):
    historial = Historial(request)
    producto = Producto.objects.get(pk=producto_id)
    historial.agregar(producto)
    return redirect("historial")

def h_eliminar_producto(request, producto_id):
    historial = Historial(request)
    producto = Producto.objects.get(pk=producto_id)
    historial.eliminar(producto)
    return redirect("historial")

def h_restar_producto(request, producto_id):
    historial = Historial(request)
    producto = Producto.objects.get(pk=producto_id)
    historial.restar(producto)
    return redirect("historial")

def h_restar_producto_n(request, producto_id, n):
    historial = Historial(request)
    producto = Producto.objects.get(pk=producto_id)
    for x in range(n):
        historial.restar(producto)
    return redirect("historial")

def h_limpiar_historial(request):
    historial = Historial(request)
    historial.limpiar()
    return redirect("historial")