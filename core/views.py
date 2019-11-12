from django.shortcuts import render
from .models import Slider,GaleriaCuerda,GaleriaPercusion,GaleriaTeclado,Nosotro

# Create your views here.

def home(request):    
    data = {
        'sliders': Slider.objects.all() # se traen los slider desde slqite
    }
    return render(request, 'core/index.html', data)

def base(request):
    return render(request, 'core/base.html')

def productos(request):
    return render(request,'core/productos.html')

def mision_vision(request):
    data = {
        'MisionVision': Nosotro.objects.all()
    }
    return render(request,'core/mision_vision.html', data)

def galeria(request):
    data = {
        'galeriaCuerda': GaleriaCuerda.objects.all(), # se traen las imagenes desde slqite
        'galeriaPercucion': GaleriaPercusion.objects.all(), 
        'galeriaTeclado': GaleriaTeclado.objects.all()
    }
    return render(request,'core/galeria.html', data)

def agregar_instrumento(request):
    return render(request, 'core/agregar_instrumento.html')

def contacto(request):
    return render(request, 'core/contacto.html')