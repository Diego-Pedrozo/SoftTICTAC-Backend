from rest_framework.viewsets import ModelViewSet
from apps.shared.models.linea_transversal import LineaTransversalModel
from apps.shared.serializers.linea_transversal import LineaTransversalSerializer

class LineaTransversalViewSet(ModelViewSet):
    model = LineaTransversalModel
    serializer_class = LineaTransversalSerializer
    queryset =  LineaTransversalModel.objects.all()


