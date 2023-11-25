from rest_framework.viewsets import ModelViewSet
from apps.shared.models.tema import TemaModel
from apps.shared.serializers.tema import TemaSerializer

class TemaViewSet(ModelViewSet):
    model = TemaModel
    serializer_class = TemaSerializer
    queryset =  TemaModel.objects.all()


