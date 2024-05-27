from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from shopyCart.Carrito import Carrito
from crud.models import Producto

def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    return render(request, "productos.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.restar(producto)
    return redirect("productos")

def restar_producto_n(request, producto_id, n):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    for x in range(n):
        carrito.restar(producto)
    return redirect("productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")