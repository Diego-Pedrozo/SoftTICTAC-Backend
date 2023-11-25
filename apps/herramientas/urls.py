from django.urls import path, include
from rest_framework import routers
from apps.herramientas.views.herramienta import HerramientaViewSet
from apps.herramientas.views.herramienta_public import HerramientaPublicViewSet


app_name = 'herramientas'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=HerramientaViewSet, prefix='herramienta', basename='herramienta')
router.register(viewset=HerramientaPublicViewSet, prefix='publico', basename='publico')


urlpatterns = [
    path('', include(router.urls))   
]