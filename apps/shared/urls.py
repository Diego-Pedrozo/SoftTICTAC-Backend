from django.urls import path, include
from rest_framework import routers
from apps.shared.views.linea_transversal import LineaTransversalViewSet
from apps.shared.views.poblacion import PoblacionViewSet
from apps.shared.views.tema import TemaViewSet
from apps.shared.views.competencia import CompetenciaViewSet

app_name = 'shared'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=LineaTransversalViewSet, prefix='lineas', basename='lineas')
router.register(viewset=PoblacionViewSet, prefix='poblaciones', basename='poblaciones')
router.register(viewset=TemaViewSet, prefix='tema', basename='tema')
router.register(viewset=CompetenciaViewSet, prefix='competencia', basename='competencia')



urlpatterns = [
    path('', include(router.urls))   
]