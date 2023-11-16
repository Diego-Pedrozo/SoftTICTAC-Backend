from django.urls import path, include
from rest_framework import routers
from apps.condigitales.views.contenido import ContenidoDigitalViewSet
from apps.condigitales.views.contenido_public import ContenidoDigitalPublicViewSet

app_name = 'condigitales'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=ContenidoDigitalViewSet, prefix='contenido', basename='contenido')
router.register(viewset=ContenidoDigitalPublicViewSet, prefix='publico', basename='publico')


urlpatterns = [
    path('', include(router.urls))   
]
