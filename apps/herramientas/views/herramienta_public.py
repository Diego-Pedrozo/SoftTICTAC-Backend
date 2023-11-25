from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.herramienta import HerramientaModel
from apps.herramientas.serializers.herramienta import HerramientaSerializer

class ContenidoDigitalPublicViewSet(ModelViewSet):
    model = HerramientaModel
    serializer_class = HerramientaSerializer
    queryset =  HerramientaModel.objects.filter(estado="Aprobado", visibilidad=True)
    http_method_names = ['get']