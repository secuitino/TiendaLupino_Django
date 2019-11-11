from django.urls import path
from .views import home,base,productos,mision_vision, galeria,agregar_instrumento,contacto
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('base/', base, name="base"),
    path('productos/', productos, name="productos"),
    path('mision_vision/', mision_vision, name="mision_vision"),
    path('galeria/', galeria, name="galeria"),
    path('agregar_instrumento/', agregar_instrumento, name="agregar_instrumento"),
    path('contacto/',contacto, name="contacto"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)