from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.recurso import RecursoModel
from apps.herramientas.serializers.recurso import RecursoSerializer

class RecursoViewSet(ModelViewSet):
    model = RecursoModel
    serializer_class = RecursoSerializer
    queryset =  RecursoModel.objects.all()


