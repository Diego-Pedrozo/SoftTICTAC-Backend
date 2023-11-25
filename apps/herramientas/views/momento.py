from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.momento import MomentoModel
from apps.herramientas.serializers.momento import MomentoSerializer

class MomentoViewSet(ModelViewSet):
    model = MomentoModel
    serializer_class = MomentoSerializer
    queryset =  MomentoModel.objects.all()


