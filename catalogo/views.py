from django.http import Http404
from django.shortcuts import render
from . import data

def productos(request):
    return render(request, 'index.html', {'productos': data.productos})

def producto_detail(request, nombre):
    producto = next((p for p in data.productos if p['nombre'] == nombre), None)
    if producto is None:
        raise Http404("Producto no encontrado")
    return render(request, 'index.html', {'producto': producto})