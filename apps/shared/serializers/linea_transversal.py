from apps.shared.models.linea_transversal import LineaTransversalModel
from rest_framework import serializers

class LineaTransversalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaTransversalModel
        fields = ['id', 'nombre']