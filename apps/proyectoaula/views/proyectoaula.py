from rest_framework.viewsets import ModelViewSet
from apps.proyectoaula.models.proyectoaula import ProyectoAulaModel
from apps.proyectoaula.serializers.proyectoaula import ProyectoAulaSerializer, ProyectoAulaUpdateSerializer
from apps.proyectoaula.models.actividad_proyecto import ActividadProyectoModel
from apps.proyectoaula.serializers.actividad_proyecto import ActividadProyectoSerializer, ActividadProyectoUpdateSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.response import Response
from datetime import date, datetime
from django.db.models import Q

class ProyectoAulaViewSet(ModelViewSet):
    model = ProyectoAulaModel
    serializer_class = ProyectoAulaSerializer
    queryset =  ProyectoAulaModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            user = self.request.user

            proyecto_data = request.data.get('proyecto', {})
            proyecto_data['user'] = user.id
            proyecto_serializer = ProyectoAulaSerializer(data=proyecto_data)

            if proyecto_serializer.is_valid():
                #print('proyecto valido')
                proyecto = proyecto_serializer.save()

                actividades_data = request.data.get('actividades', [])
                for actividad_data in actividades_data:
                        actividad_data['id_proyectoaula'] = proyecto.id
                        actividad_serializer = ActividadProyectoSerializer(data=actividad_data)
                        if actividad_serializer.is_valid():
                            #print('actividad valida')
                            actividad = actividad_serializer.save()
                        else:
                            proyecto.delete()
                            return Response({
                            'status': 'Error',
                            'message': f'Error al crear actividad: {actividad_serializer.errors}'
                            }, status=status.HTTP_400_BAD_REQUEST)

                return Response({
                            'status': 'OK',
                            'message': 'Proyecto de aula creado exitosamente.',
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'Error',
                    'message': 'Error en los datos del proyecto.',
                    'errors': proyecto_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        user = self.request.user
       
        if(user != self.get_object().user):
            return Response({'mensaje': 'No tiene permisos para editar esta herramienta'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            proyecto_instance = self.get_object()
            proyecto_data = request.data.get('proyecto')
            actividades_data = request.data.get('actividades')

            if 'lecciones_aprendidas' in proyecto_data:
                proyecto_data['fecha_fin'] = datetime.now().strftime('%Y-%m-%d')
            else:
                proyecto_data['fecha_fin'] = None
                proyecto_data['lecciones_aprendidas'] = None
                
            proyecto_serializer = ProyectoAulaUpdateSerializer(data=proyecto_data)
            if proyecto_serializer.is_valid():
                proyecto = ProyectoAulaSerializer(instance=proyecto_instance, data=proyecto_data, partial=True)         
                if proyecto.is_valid():
                    proyecto.save()
            
            for actividad_data in actividades_data:
                if 'cumplimiento' in actividad_data and actividad_data['cumplimiento'] == True:
                    actividad_data['fecha_fin'] = datetime.now().strftime('%Y-%m-%d')
                elif 'cumplimiento' in actividad_data and actividad_data['cumplimiento'] == False:
                    actividad_data['fecha_fin'] = None
                    actividad_data['observaciones'] = None
                    
                actividad_serializer = ActividadProyectoUpdateSerializer(data=actividad_data)
                if actividad_serializer.is_valid():
                    actividad_instance = ActividadProyectoModel.objects.get(id_proyectoaula=proyecto_instance, id=actividad_data['id'])
                    actividad = ActividadProyectoSerializer(instance=actividad_instance, data=actividad_data, partial=True)       
                    if actividad.is_valid():
                        actividad.save()
            
            return Response({'mensaje': 'Proyecto aula actualizado'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'mensaje': 'Error al actualizar el proyecto', 'error': {str(e)}}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = request.user

        if instance.user != user:
            return Response({'mensaje': 'No tiene permisos para eliminar este proyecto de aula.'}, status=status.HTTP_403_FORBIDDEN)
        
        proyectoaula_id = instance.id
        ProyectoAulaModel.objects.filter(id=proyectoaula_id).delete()

        return Response({'mensaje': 'Proyuecto de aula eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
