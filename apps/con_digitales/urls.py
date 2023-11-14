from django.urls import path, include
from rest_framework import routers

app_name = 'con_digitales'
router = routers.DefaultRouter()
##Configurar rutas 


urlpatterns = [
    path('', include(router.urls))   
]
