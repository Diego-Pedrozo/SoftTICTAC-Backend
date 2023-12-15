from django.urls import path, include
from rest_framework import routers

from apps.user.views.user import UserViewSet

app_name = 'core'
router = routers.DefaultRouter()
router.register(viewset=UserViewSet, basename='user', prefix='user')
##Configurar rutas 
#
#
#

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    #path('user/', include('apps.user.urls')),
    path('contenidos/', include('apps.condigitales.urls')),
    path('herramientas/', include('apps.herramientas.urls')),
    path('shared/', include('apps.shared.urls')),
    path('proyectoaula/', include('apps.proyectoaula.urls')),
    path('plantrabajo/', include('apps.plantrabajo.urls')),
    path('estadisticas/', include('apps.estadisticas.urls')),
    path('', include(router.urls))   
]
