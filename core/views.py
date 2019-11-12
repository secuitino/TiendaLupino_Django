from django.shortcuts import render
from .models import Slider,GaleriaCuerda,GaleriaPercusion,GaleriaTeclado

# Create your views here.

def home(request):    
    data = {
        'sliders': Slider.objects.all()
    }
    return render(request, 'core/index.html', data)

def base(request):
    return render(request, 'core/base.html')

def productos(request):
    return render(request,'core/productos.html')

def mision_vision(request):
    return render(request,'core/mision_vision.html')

def galeria(request):
    data = {
        'galeriaCuerda': GaleriaCuerda.objects.all(), 
        'galeriaPercusion': GaleriaPercusion.objects.all(),
        'galeriaTeclado': GaleriaTeclado.objects.all()  
    }
    return render(request, 'core/galeria.html', data)

def agregar_instrumento(request):
    return render(request, 'core/agregar_instrumento.html', data)

def contacto(request):
    return render(request, 'core/contacto.html')