from apps.shared.models.tema import TemaModel
from rest_framework import serializers
from apps.shared.serializers.competencia import CompetenciaSerializer

class TemaSerializer(serializers.ModelSerializer):
    id_competencia = CompetenciaSerializer(many=True, read_only=True)
    
    class Meta:
        model = TemaModel
        fields = ['id', 'nombre', 'id_linea', 'id_competencia']

class TemaUpdateSerializer(serializers.ModelSerializer):
    id_competencia = CompetenciaSerializer(many=True, read_only=True)
    
    class Meta:
        model = TemaModel
        fields = ['nombre', 'id_linea', 'id_competencia']

    def get_id_competencia(self, obj):
        return [{'id': competencia.id} for competencia in obj.id_competencia.all()]