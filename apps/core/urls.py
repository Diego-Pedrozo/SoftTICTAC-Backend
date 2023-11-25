from django.urls import path, include
from rest_framework import routers

app_name = 'core'
router = routers.DefaultRouter()
##Configurar rutas 
#
#
#

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('user/', include('apps.user.urls')),
    path('contenidos/', include('apps.condigitales.urls')),
    path('herramientas/', include('apps.herramientas.urls')),
    path('shared/', include('apps.shared.urls')),
    path('', include(router.urls))   
]
