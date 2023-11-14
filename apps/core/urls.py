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
    path('', include(router.urls))   
]
