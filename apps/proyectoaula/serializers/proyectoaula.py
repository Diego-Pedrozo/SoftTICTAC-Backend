from apps.proyectoaula.models.proyectoaula import ProyectoAulaModel
from apps.proyectoaula.serializers.actividad import ActividadSerializer
from rest_framework import serializers


class ProyectoAulaSerializer(serializers.ModelSerializer):
    actividades = ActividadSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProyectoAulaModel
        fields = ['id', 'user', 'id_linea', 'nombre', 'grado', 'fecha_inicio', 'fecha_fin',
                  'lecciones_aprendidas', 'actividades']
        
class ProyectoAulaUpdateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ProyectoAulaModel
        fields = ['nombre', 'fecha_fin', 'lecciones_aprendidas']
        
