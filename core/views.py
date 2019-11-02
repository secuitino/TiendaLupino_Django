from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def base(request):
    return render(request, 'core/base.html')

def productos(request):
    return render(request,'core/productos.html')

def mision_vision(request):
    return render(request,'core/mision_vision.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def agregar_instrumento(request):
    return render(request, 'core/agregar_instrumento.html')

def contacto(request):
    return render(request, 'core/contacto.html')