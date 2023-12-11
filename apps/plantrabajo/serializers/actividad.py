from apps.plantrabajo.models.actividad import ActividadModel
from rest_framework import serializers

class ActividadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadModel
        fields = ['id', 'id_plan', 'nombre', 'docentes',
                  'cumplimiento', 'observaciones', 'fecha_inicio', 'fecha_fin']
        
class ActividadUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadModel
        fields = ['nombre', 'docentes',
                  'cumplimiento', 'observaciones', 'fecha_fin']
        
        
