from django.urls import path, include
from rest_framework import routers
from apps.herramientas.views.herramienta import HerramientaViewSet


app_name = 'herramientas'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=HerramientaViewSet, prefix='herramienta', basename='herramienta')


urlpatterns = [
    path('', include(router.urls))   
]