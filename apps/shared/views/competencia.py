from rest_framework.viewsets import ModelViewSet
from apps.shared.models.competencia import CompetenciaModel
from apps.shared.serializers.competencia import CompetenciaSerializer

class CompetenciaViewSet(ModelViewSet):
    model = CompetenciaModel
    serializer_class = CompetenciaSerializer
    queryset =  CompetenciaModel.objects.all()


