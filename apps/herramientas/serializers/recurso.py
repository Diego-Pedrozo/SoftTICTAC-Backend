from apps.herramientas.models.recurso import RecursoModel
from rest_framework import serializers

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoModel
        fields = ['id', 'tipo']