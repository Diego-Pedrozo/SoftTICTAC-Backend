from rest_framework.viewsets import ModelViewSet
from apps.condigitales.models.contenido import ContenidoDigitalModel
from apps.condigitales.serializers.contenido import ContenidoDigitalSerializer

class ContenidoDigitalPublicViewSet(ModelViewSet):
    model = ContenidoDigitalModel
    serializer_class = ContenidoDigitalSerializer
    queryset =  ContenidoDigitalModel.objects.filter(estado="Aprobado", visibilidad=True)
    http_method_names = ['get']