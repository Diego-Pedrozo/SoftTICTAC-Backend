from rest_framework.viewsets import ModelViewSet
from apps.proyectoaula.models.proyectoaula import ProyectoAulaModel
from apps.proyectoaula.serializers.proyectoaula import ProyectoAulaSerializer

class ProyectoAulaPublicViewSet(ModelViewSet):
    model = ProyectoAulaModel
    serializer_class = ProyectoAulaSerializer
    queryset =  ProyectoAulaModel.objects.all()
    http_method_names = ['get']
