from apps.plantrabajo.models.plantrabajo import PlanTrabajoModel
from apps.plantrabajo.serializers.actividad import ActividadSerializer
from rest_framework import serializers


class PlanTrabajoSerializer(serializers.ModelSerializer):
    actividades = ActividadSerializer(many=True, read_only=True)
    
    class Meta:
        model = PlanTrabajoModel
        fields = ['id', 'user', 'id_linea', 'nombre', 'año',
                  'lecciones_aprendidas', 'actividades']
        
class PlanTrabajoUpdateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = PlanTrabajoModel
        fields = ['nombre', 'año', 'lecciones_aprendidas']
        
