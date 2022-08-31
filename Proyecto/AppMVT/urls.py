from django.urls import path
from .views import * 


urlpatterns = [
    path('', inicio, name='inicio'),
    path('Prestadores/',prestadores, name='prestadores'),
    path('Leyes/', leyes, name='leyes'),
    path('Cobertura/', Cobertura_salud, name='cobertura'),
    path('Familia/', familia_vinculo, name='familia'),
    path('Trabajo/', trabajo_titular, name='trabajo'),
    path('Conocenos/', conocenos, name='conocenos'),
    path('Quienes_somos?/', quienes_somos, name='quienes_somos'),
    path('formularioFamilia/', formularioFamilia, name='formularioFamilia'),
   
]