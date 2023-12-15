from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.herramienta import HerramientaModel
from apps.herramientas.serializers.herramienta import HerramientaSerializer, HerramientaCreateSerializer, HerramientaUpdateSerializer
from apps.shared.models.tema import TemaModel
from apps.shared.serializers.tema import TemaSerializer, TemaUpdateSerializer
from apps.herramientas.serializers.momento import MomentoSerializer, MomentoUpdateSerializer
from apps.herramientas.models.momento import MomentoModel
from apps.herramientas.serializers.proceso import ProcesoSerializer, ProcesoUpdateSerializer
from apps.herramientas.models.proceso import ProcesoModel

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from apps.estadisticas.models.stats import UserStatsModel
from rest_framework.response import Response
from datetime import date, datetime
from django.db.models import Q

class HerramientaViewSet(ModelViewSet):
    model = HerramientaModel
    serializer_class = HerramientaSerializer
    queryset =  HerramientaModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    # def get_serializer_class(self):
    #     serializer_mapping = {
    #         'create': HerramientaCreateSerializer,
    #         'partial_update': HerramientaSerializer,
    #         #'put': HerramientaUpdateSerializer,
    #         #'update': HerramientaSerializer
    #     }
    #     return serializer_mapping.get(self.action, super().get_serializer_class())

    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            user = self.request.user
            
            tema_data = request.data.get('tema', {})
            tema_serializer = TemaSerializer(data=tema_data)

            if tema_serializer.is_valid():
                tema = tema_serializer.save()

                competencias_data = tema_data.get('id_competencia', [])
                competencia_ids = [competencia['id'] for competencia in competencias_data]
                tema.id_competencia.set(competencia_ids)
                
                herramienta_data = request.data.get('herramienta', {})
                herramienta_data['id_tema'] = tema.id
                herramienta_data['user'] = user.id
                herramienta_data['fecha_creacion'] = datetime.now()
                herramienta_serializer = HerramientaCreateSerializer(data=herramienta_data)

                if herramienta_serializer.is_valid():
                    herramienta = herramienta_serializer.save()

                    poblaciones_data = herramienta_data.get('id_poblacion', [])
                    poblacion_ids = [poblacion['id'] for poblacion in poblaciones_data]
                    herramienta.id_poblacion.set(poblacion_ids)

                    momentos_data = request.data.get('momentos', [])
                    for momento_data in momentos_data:
                        momento_data['id_herramienta'] = herramienta.id
                        momento_serializer = MomentoSerializer(data=momento_data)
                        if momento_serializer.is_valid():
                            momento = momento_serializer.save()

                            if momento.nombre == "Desarrollo":
                                procesos_data = momento_data.get('procesos', [])
                                for proceso_data in procesos_data:
                                    proceso_data['id_momento'] = momento.id
                                    proceso_serializer = ProcesoSerializer(data=proceso_data)
                                    if proceso_serializer.is_valid():
                                        proceso = proceso_serializer.save()

                                        # recursos_data = proceso_data.get('recursos', [])
                                        # recursos_ids = [recurso['id'] for recurso in recursos_data]
                                        # proceso.id_recurso.set(recursos_ids)
                                    else:
                                        tema.delete()
                                        return Response({
                                            'status': 'Error',
                                            'message': f'Error al crear el proceso: {proceso_serializer.errors}'
                                        }, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            tema.delete()
                            return Response({
                                'status': 'Error',
                                'message':'Error al crear el momento.',
                                'errors': momento_serializer.errors
                            }, status=status.HTTP_400_BAD_REQUEST)
                    
                    return Response({
                        'status': 'OK',
                        'message': 'Herramienta creada exitosamente.',
                    }, status=status.HTTP_201_CREATED)
                else:
                    tema.delete()
                    return Response({
                        'status': 'Error',
                        'message': 'Error en los datos de la herramienta.',
                        'errors': herramienta_serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'status': 'Error',
                    'message': 'Error en los datos del tema.',
                    'errors': tema_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
                    
        except Exception as e:
            tema.delete()
            return Response({'message': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = self.request.user
        user_information = UserInformationModel.objects.get(user=user)
        mutable_data = request.data
        contenido_serializer = HerramientaSerializer(data=mutable_data)

        if user_information.user_type not in ['1', '2', '3', '4', '5', '6']:
            return Response({'mensaje': 'No tiene permisos para cambiar el estado de esta herramienta.'}, status=status.HTTP_403_FORBIDDEN)

        if instance.estado == 'Pendiente' and user_information.user_type in ['1', '2', '3', '4', '5']:
            if request.data.get('estado') == 'Aprobado' and 'fecha_aprobacion' not in request.data:
                instance.fecha_aprobacion = datetime.now()
                instance.save()
                #aumenta stats de herramienta del usuario creador
                user_herramienta = instance.user
                user_stats = UserStatsModel.objects.get(user=user_herramienta)
                tema_herramienta = TemaModel.objects.get(id=instance.id_tema.id)
                id_linea = tema_herramienta.id_linea.id
                if id_linea == 1:
                    user_stats.herramientas_emprendimiento = user_stats.herramientas_emprendimiento+1
                    user_stats.save()
                elif id_linea == 2:
                    user_stats.herramientas_sexualidad = user_stats.herramientas_sexualidad+1
                    user_stats.save()
                elif id_linea == 3:
                    user_stats.herramientas_relaciones_sociales = user_stats.herramientas_relaciones_sociales+1
                    user_stats.save()
                elif id_linea == 4:
                    user_stats.herramientas_medio_ambiente = user_stats.herramientas_medio_ambiente+1
                    user_stats.save()
                elif id_linea == 5:
                    user_stats.herramientas_tics = user_stats.herramientas_tics+1
                    user_stats.save()
                return super().partial_update(request, *args, **kwargs)
            elif request.data.get('estado') == 'Rechazado':
                return super().partial_update(request, *args, **kwargs)
            else:
                return Response({'mensaje': 'No puede editar en este momento1'})
                
        elif instance.estado in ['Rechazado', 'Aprobado'] and user_information.user_type in ['1', '2', '3', '4', '5', '6']:
            if request.data.get('estado') in ['Rechazado', 'Aprobado'] and user_information.user_type in ['1', '2', '3', '4', '5']:
                return Response({'mensaje': 'No puede editar en este momento2'}, status=status.HTTP_200_OK)
            elif request.data.get('estado') not in ['Pendiente']:
                instance.estado = 'Pendiente'
                instance.fecha_aprobacion = None
                instance.save()
                return super().partial_update(request, *args, **kwargs)
            else:
                return Response({'mensaje': 'No puede editar en este momento3'}, status=status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'No puede editar en este momento4'}, status=status.HTTP_200_OK)
    
    
    def list(self, request, *args, **kwargs):
        print(self.action)
        user = request.user
        estado = request.query_params.get('estado', None)
        user_information = UserInformationModel.objects.get(user=user)
         
        if estado == 'Pendiente' and user_information.user_type in ['6']:
            queryset = HerramientaModel.objects.filter(estado="Pendiente", user=user)
        
        elif estado == 'Pendiente' and user_information.user_type in ['1', '2', '3', '4', '5']:
            queryset = HerramientaModel.objects.filter(Q(estado="Pendiente") &
                                                       (Q(id_tema__id_linea=user_information.user_type) |
                                                        Q(user=user)))

        elif estado == 'Rechazado' and user_information.user_type in ['1', '2', '3', '4', '5', '6']:
            queryset = HerramientaModel.objects.filter(estado="Rechazado", user=user)

        elif estado == 'Aprobado':
            queryset = HerramientaModel.objects.filter(estado="Aprobado")

        else:
            queryset = []

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = request.user

        if instance.user != user:
            return Response({'mensaje': 'No tiene permisos para eliminar esta herramienta.'}, status=status.HTTP_403_FORBIDDEN)
        
        tema_id = instance.id_tema.id
        TemaModel.objects.filter(id=tema_id).delete()

        return Response({'mensaje': 'Herramienta eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
