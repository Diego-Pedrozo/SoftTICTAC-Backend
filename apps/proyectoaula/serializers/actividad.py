from apps.proyectoaula.models.actividad import ActividadModel
from rest_framework import serializers

class ActividadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadModel
        fields = ['id', 'id_proyectoaula', 'nombre', 'descripcion', 'estudiantes',
                  'cumplimiento', 'observaciones', 'fecha_inicio', 'fecha_fin']
        
class ActividadUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadModel
        fields = ['nombre', 'descripcion', 'estudiantes',
                  'cumplimiento', 'observaciones', 'fecha_fin']
        
        
