from django.urls import path, include
from rest_framework import routers
from apps.plantrabajo.views.plantrabajo import PlanTrabajoViewSet

app_name = 'plantrabajo'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(viewset=PlanTrabajoViewSet, prefix='plan', basename='plan')

urlpatterns = [
    path('', include(router.urls))   
]