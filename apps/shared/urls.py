from django.urls import path, include
from rest_framework import routers
from apps.shared.views.linea_transversal import LineaTransversalViewSet
from apps.shared.views.poblacion import PoblacionViewSet

app_name = 'shared'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=LineaTransversalViewSet, prefix='lineas', basename='lineas')
router.register(viewset=PoblacionViewSet, prefix='poblaciones', basename='poblaciones')



urlpatterns = [
    path('', include(router.urls))   
]