from apps.shared.models.competencia import CompetenciaModel
from rest_framework import serializers

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenciaModel
        fields = ['id']