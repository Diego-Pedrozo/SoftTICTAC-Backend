from apps.shared.models.poblacion import PoblacionModel
from rest_framework import serializers

class PoblacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoblacionModel
        fields = ['id', 'nombre']