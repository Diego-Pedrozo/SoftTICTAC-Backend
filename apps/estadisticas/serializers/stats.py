from apps.estadisticas.models.stats import UserStatsModel
from rest_framework import serializers

class UserStatsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserStatsModel
        fields = ['id', 'user', 'proyectos_emprendimiento', 'proyectos_sexualidad', 'proyectos_relaciones_sociales', 'proyectos_medio_ambiente', 'proyectos_tics',
                  'contenidos_emprendimiento', 'contenidos_sexualidad', 'contenidos_relaciones_sociales', 'contenidos_medio_ambiente', 'contenidos_tics',
                  'herramientas_emprendimiento', 'herramientas_sexualidad', 'herramientas_relaciones_sociales', 'herramientas_medio_ambiente', 'herramientas_tics'
                  ]

class TopDocentesProyectosSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    total_proyectos = serializers.IntegerField()

    class Meta:
        model = UserStatsModel
        fields = ['user', 'total_proyectos']

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
            'nombre': user.first_name,
            'apellido': user.last_name,
        }

class TopDocentesHerramientasSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    total_herramientas = serializers.IntegerField()

    class Meta:
        model = UserStatsModel
        fields = ['user', 'total_herramientas']

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
            'nombre': user.first_name,
            'apellido': user.last_name,
        }

class TopDocentesContenidosSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    total_contenidos = serializers.IntegerField()

    class Meta:
        model = UserStatsModel
        fields = ['user', 'total_contenidos']

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
            'nombre': user.first_name,
            'apellido': user.last_name,
        }