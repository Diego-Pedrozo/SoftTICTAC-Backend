from django.urls import path, include
from rest_framework import routers
from apps.proyectoaula.views.proyectoaula import ProyectoAulaViewSet
from apps.proyectoaula.views.proyectoaula_public import ProyectoAulaPublicViewSet

app_name = 'proyectoaula'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=ProyectoAulaViewSet, prefix='proyecto', basename='proyecto')
router.register(viewset=ProyectoAulaPublicViewSet, prefix='publico', basename='publico')

urlpatterns = [
    path('', include(router.urls))   
]