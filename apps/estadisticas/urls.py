from django.urls import path, include
from rest_framework import routers
from apps.estadisticas.views.stats import (UserStatsViewSet, CantidadProyectosView, TopDocentesProyectosViewSet, 
                                           CantidadHerramientasView, TopDocentesHerramientasViewSet, 
                                           CantidadContenidosView, TopDocentesContenidosViewSet)

app_name = 'estadisticas'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=UserStatsViewSet, prefix='stats', basename='stats')
router.register(viewset=TopDocentesProyectosViewSet, prefix='topproyectos', basename='topproyectos')
router.register(viewset=TopDocentesHerramientasViewSet, prefix='topherramientas', basename='topherramientas')
router.register(viewset=TopDocentesContenidosViewSet, prefix='topcontenidos', basename='topcontenidos')

urlpatterns = [
    path('proyectos/', CantidadProyectosView.as_view(), name='cantidad_proyectos'),
    path('herramientas/', CantidadHerramientasView.as_view(), name='cantidad_herramientas'),
    path('contenidos/', CantidadContenidosView.as_view(), name='cantidad_contenidos'),
    path('', include(router.urls))   
]