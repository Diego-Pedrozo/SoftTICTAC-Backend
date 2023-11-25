from apps.herramientas.models.herramienta import HerramientaModel
from rest_framework import serializers
from apps.herramientas.serializers.momento import MomentoSerializer
from apps.shared.serializers.tema import TemaSerializer

class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HerramientaModel
        fields = ['id', 'user', 'id_tema', 'nombre', 'objetivo', 'visibilidad', 'estado',
                   'recomendacion', 'revision', 'fecha_creacion', 'fecha_aprobacion', 'id_poblacion', 'duracion']