from rest_framework.viewsets import ModelViewSet
from apps.shared.models.poblacion import PoblacionModel
from apps.shared.serializers.poblacion import PoblacionSerializer

class PoblacionViewSet(ModelViewSet):
    model = PoblacionModel
    serializer_class = PoblacionSerializer
    queryset =  PoblacionModel.objects.all()


