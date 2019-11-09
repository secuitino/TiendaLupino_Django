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

