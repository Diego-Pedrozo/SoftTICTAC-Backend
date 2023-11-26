from apps.herramientas.models.momento import MomentoModel
from rest_framework import serializers
from apps.herramientas.serializers.proceso import ProcesoSerializer

class MomentoSerializer(serializers.ModelSerializer):
    procesos = ProcesoSerializer(many=True, read_only=True)

    class Meta:
        model = MomentoModel
        fields = ['id', 'id_herramienta', 'nombre', 'descripcion', 'procesos']

class MomentoUpdateSerializer(serializers.ModelSerializer):
    #procesos = ProcesoSerializer(many=True, read_only=True)

    class Meta:
        model = MomentoModel
        fields = ['nombre', 'descripcion']