from rest_framework.viewsets import ModelViewSet
from apps.estadisticas.models.stats import UserStatsModel
from apps.estadisticas.serializers.stats import UserStatsSerializer, TopDocentesProyectosSerializer, TopDocentesHerramientasSerializer, TopDocentesContenidosSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from rest_framework.views import APIView
from django.db.models import F

class UserStatsViewSet(ModelViewSet):
    model = UserStatsModel
    serializer_class = UserStatsSerializer
    #queryset =  UserStatsModel.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        return UserStatsModel.objects.filter(user=self.request.user)
    
class CantidadProyectosView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        total_emprendimiento = UserStatsModel.objects.aggregate(total_emprendimiento=Sum('proyectos_emprendimiento'))['total_emprendimiento']
        total_sexualidad = UserStatsModel.objects.aggregate(total_sexualidad=Sum('proyectos_sexualidad'))['total_sexualidad']
        total_relaciones_sociales = UserStatsModel.objects.aggregate(total_relaciones_sociales=Sum('proyectos_relaciones_sociales'))['total_relaciones_sociales']
        total_medio_ambiente = UserStatsModel.objects.aggregate(total_medio_ambiente=Sum('proyectos_medio_ambiente'))['total_medio_ambiente']
        total_tics = UserStatsModel.objects.aggregate(total_tics=Sum('proyectos_tics'))['total_tics']

        totales = {
            'total_proyectos_emprendimiento': total_emprendimiento,
            'total_proyectos_sexualidad': total_sexualidad,
            'total_proyectos_relaciones_sociales': total_relaciones_sociales,
            'total_proyectos_medio_ambiente': total_medio_ambiente,
            'total_proyectos_tics': total_tics,
        }
        return Response(totales, status=status.HTTP_200_OK)

    
class TopDocentesProyectosViewSet(ModelViewSet):
    model = UserStatsModel
    http_method_names = ['get']
    serializer_class = TopDocentesProyectosSerializer

    def get_queryset(self):
        try:
            queryset = UserStatsModel.objects.annotate(
                total_proyectos=(
                    F('proyectos_emprendimiento') +
                    F('proyectos_sexualidad') +
                    F('proyectos_relaciones_sociales') +
                    F('proyectos_medio_ambiente') +
                    F('proyectos_tics')
                )
            ).order_by('-total_proyectos')[:3]
            return queryset
        except Exception as e:
            return Response({'mensaje': 'Error al obtener los docentes', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CantidadHerramientasView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        total_emprendimiento = UserStatsModel.objects.aggregate(total_emprendimiento=Sum('herramientas_emprendimiento'))['total_emprendimiento']
        total_sexualidad = UserStatsModel.objects.aggregate(total_sexualidad=Sum('herramientas_sexualidad'))['total_sexualidad']
        total_relaciones_sociales = UserStatsModel.objects.aggregate(total_relaciones_sociales=Sum('herramientas_relaciones_sociales'))['total_relaciones_sociales']
        total_medio_ambiente = UserStatsModel.objects.aggregate(total_medio_ambiente=Sum('herramientas_medio_ambiente'))['total_medio_ambiente']
        total_tics = UserStatsModel.objects.aggregate(total_tics=Sum('herramientas_tics'))['total_tics']

        totales = {
            'total_herramientas_emprendimiento': total_emprendimiento,
            'total_herramientas_sexualidad': total_sexualidad,
            'total_herramientas_relaciones_sociales': total_relaciones_sociales,
            'total_herramientas_medio_ambiente': total_medio_ambiente,
            'total_herramientas_tics': total_tics,
        }
        return Response(totales, status=status.HTTP_200_OK)

class TopDocentesHerramientasViewSet(ModelViewSet):
    model = UserStatsModel
    http_method_names = ['get']
    serializer_class = TopDocentesHerramientasSerializer

    def get_queryset(self):
        try:
            queryset = UserStatsModel.objects.annotate(
                total_herramientas=(
                    F('herramientas_emprendimiento') +
                    F('herramientas_sexualidad') +
                    F('herramientas_relaciones_sociales') +
                    F('herramientas_medio_ambiente') +
                    F('herramientas_tics')
                )
            ).order_by('-total_herramientas')[:3]
            return queryset
        except Exception as e:
            return Response({'mensaje': 'Error al obtener los docentes', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class CantidadContenidosView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        total_emprendimiento = UserStatsModel.objects.aggregate(total_emprendimiento=Sum('contenidos_emprendimiento'))['total_emprendimiento']
        total_sexualidad = UserStatsModel.objects.aggregate(total_sexualidad=Sum('contenidos_sexualidad'))['total_sexualidad']
        total_relaciones_sociales = UserStatsModel.objects.aggregate(total_relaciones_sociales=Sum('contenidos_relaciones_sociales'))['total_relaciones_sociales']
        total_medio_ambiente = UserStatsModel.objects.aggregate(total_medio_ambiente=Sum('contenidos_medio_ambiente'))['total_medio_ambiente']
        total_tics = UserStatsModel.objects.aggregate(total_tics=Sum('contenidos_tics'))['total_tics']

        totales = {
            'total_contenidos_emprendimiento': total_emprendimiento,
            'total_contenidos_sexualidad': total_sexualidad,
            'total_contenidos_relaciones_sociales': total_relaciones_sociales,
            'total_contenidos_medio_ambiente': total_medio_ambiente,
            'total_contenidos_tics': total_tics,
        }
        return Response(totales, status=status.HTTP_200_OK)

class TopDocentesContenidosViewSet(ModelViewSet):
    model = UserStatsModel
    http_method_names = ['get']
    serializer_class = TopDocentesContenidosSerializer

    def get_queryset(self):
        try:
            queryset = UserStatsModel.objects.annotate(
                total_contenidos=(
                    F('contenidos_emprendimiento') +
                    F('contenidos_sexualidad') +
                    F('contenidos_relaciones_sociales') +
                    F('contenidos_medio_ambiente') +
                    F('contenidos_tics')
                )
            ).order_by('-total_contenidos')[:3]
            return queryset
        except Exception as e:
            return Response({'mensaje': 'Error al obtener los docentes', 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)