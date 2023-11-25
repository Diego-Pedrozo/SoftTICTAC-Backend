from apps.herramientas.models.proceso import ProcesoModel
from rest_framework import serializers
from apps.herramientas.serializers.recurso import RecursoSerializer

class ProcesoSerializer(serializers.ModelSerializer):
    id_recurso = RecursoSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProcesoModel
        fields = ['id', 'id_momento', 'nombre', 'descripcion', 'tiempo', 'id_recurso']