from django.db import models

# Create your models here.

class TipoInstrumento(models.Model):

    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Instrumento(models.Model):
    nombre = models.CharField(max_length=80)
    tipoInstrumento = models.ForeignKey(TipoInstrumento, on_delete=models.CASCADE, blank=True, null=True)
    precio = models.IntegerField(blank=True)
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Slider(models.Model):
    image = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class GaleriaCuerda(models.Model):
    imagen= models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class GaleriaTeclado(models.Model):
    imagen= models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class GaleriaPercusion(models.Model):
    imagen= models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Nosotro(models.Model):
    titulo_pagina = models.CharField(max_length=80)
    titulo_mision = models.TextField(max_length=300)
    descripcion_mision = models.TextField(max_length=1000)
    titulo_vision = models.TextField(max_length=300)
    descripcion_vision = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo_pagina  
