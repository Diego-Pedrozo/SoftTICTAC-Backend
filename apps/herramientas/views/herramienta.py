from rest_framework.viewsets import ModelViewSet
from apps.herramientas.models.herramienta import HerramientaModel
from apps.herramientas.serializers.herramienta import HerramientaSerializer
from apps.shared.models.tema import TemaModel
from apps.shared.serializers.tema import TemaSerializer
from apps.herramientas.serializers.momento import MomentoSerializer
from apps.herramientas.serializers.proceso import ProcesoSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.response import Response
from datetime import date, datetime

class HerramientaViewSet(ModelViewSet):
    model = HerramientaModel
    serializer_class = HerramientaSerializer
    queryset =  HerramientaModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

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
                herramienta_serializer = HerramientaSerializer(data=herramienta_data)

                if herramienta_serializer.is_valid():
                    herramienta = herramienta_serializer.save()

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

                                        recursos_data = proceso_data.get('recursos', [])
                                        recursos_ids = [recurso['id'] for recurso in recursos_data]
                                        proceso.id_recurso.set(recursos_ids)
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

    # def partial_update(self, request, *args, **kwargs):
    #     print(self.action)
    #     instance = self.get_object()
    #     user = self.request.user
    #     user_information = UserInformationModel.objects.get(user=user)

    #     if user_information.user_type not in ['2', '3']:
    #         return Response({'mensaje': 'No tiene permisos para cambiar el estado de este contenido.'}, status=status.HTTP_403_FORBIDDEN)

    #     if instance.estado == 'Pendiente' and user_information.user_type in ['2']:
    #         if request.data.get('estado') == 'Aprobado' and 'fecha_aprobacion' not in request.data:
    #             request.data['fecha_aprobacion'] = datetime.now()
            
    #         return super().partial_update(request, *args, **kwargs)
                
    #     elif instance.estado in ['Rechazado', 'Aprobado'] and user_information.user_type in ['2', '3']:
    #         request.data['estado'] = 'Pendiente'
    #         request.data['fecha_aprobacion'] = None
    #         return super().partial_update(request, *args, **kwargs)
            
    
    def list(self, request, *args, **kwargs):
        print(self.action)
        user = request.user
        estado = request.query_params.get('estado', None)
        user_information = UserInformationModel.objects.get(user=user)
         
        if estado == 'Pendiente' and user_information.user_type in ['2']:
            queryset = HerramientaModel.objects.filter(estado="Pendiente")

        elif estado == 'Rechazado' and user_information.user_type in ['2', '3']:
            queryset = HerramientaModel.objects.filter(estado="Rechazado", user=user)

        elif estado == 'Aprobado':
            queryset = HerramientaModel.objects.filter(estado="Aprobado")

        else:
            queryset = ""

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