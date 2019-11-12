from django.contrib import admin
from .models import Instrumento, TipoInstrumento, Slider,GaleriaCuerda,GaleriaPercusion,GaleriaTeclado,Nosotro
# Register your models here.


class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipoInstrumento','precio','descripcion','stock']
    search_fields = ['nombre', 'tipoInstrumento','precio','descripcion','stock']
    list_filter = ['nombre', 'tipoInstrumento','precio','descripcion','stock']
    list_per_page = 10



admin.site.register (TipoInstrumento)
admin.site.register (Instrumento, InstrumentoAdmin)
admin.site.register(Slider)
admin.site.register(GaleriaCuerda)
admin.site.register(GaleriaPercusion)
admin.site.register(GaleriaTeclado)
admin.site.register(Nosotro)


