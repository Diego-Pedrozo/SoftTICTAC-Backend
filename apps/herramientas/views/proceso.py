from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.proceso import ProcesoModel
from apps.herramientas.serializers.proceso import ProcesoSerializer

class ProcesoViewSet(ModelViewSet):
    model = ProcesoModel
    serializer_class = ProcesoSerializer
    queryset =  ProcesoModel.objects.all()


