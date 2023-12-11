from apps.proyectoaula.models.actividad_proyecto import ActividadProyectoModel
from rest_framework import serializers

class ActividadProyectoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadProyectoModel
        fields = ['id', 'id_proyectoaula', 'nombre', 'descripcion', 'estudiantes',
                  'cumplimiento', 'observaciones', 'fecha_inicio', 'fecha_fin']
        
class ActividadProyectoUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadProyectoModel
        fields = ['nombre', 'descripcion', 'estudiantes',
                  'cumplimiento', 'observaciones', 'fecha_fin']
        
        
