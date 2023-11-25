from apps.herramientas.models.momento import MomentoModel
from rest_framework import serializers
from apps.herramientas.serializers.proceso import ProcesoSerializer

class MomentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentoModel
        fields = ['id', 'id_herramienta', 'nombre', 'descripcion']