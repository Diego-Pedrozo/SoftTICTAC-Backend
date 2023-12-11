from rest_framework.viewsets import ModelViewSet
from apps.plantrabajo.models.plantrabajo import PlanTrabajoModel
from apps.plantrabajo.serializers.plantrabajo import PlanTrabajoSerializer, PlanTrabajoUpdateSerializer
from apps.plantrabajo.models.actividad import ActividadModel
from apps.plantrabajo.serializers.actividad import ActividadSerializer, ActividadUpdateSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.response import Response
from datetime import date, datetime
from django.db.models import Q

class PlanTrabajoViewSet(ModelViewSet):
    model = PlanTrabajoModel
    serializer_class = PlanTrabajoSerializer
    queryset =  PlanTrabajoModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            user = self.request.user

            plan_data = request.data.get('plan', {})
            plan_data['user'] = user.id
            plan_serializer = PlanTrabajoSerializer(data=plan_data)

            if plan_serializer.is_valid():
                #print('plan valido')
                plan = plan_serializer.save()

                actividades_data = request.data.get('actividades', [])
                for actividad_data in actividades_data:
                        actividad_data['id_plan'] = plan.id
                        actividad_serializer = ActividadSerializer(data=actividad_data)
                        if actividad_serializer.is_valid():
                            #print('actividad valida')
                            actividad = actividad_serializer.save()
                        else:
                            plan.delete()
                            return Response({
                            'status': 'Error',
                            'message': f'Error al crear actividad: {actividad_serializer.errors}'
                            }, status=status.HTTP_400_BAD_REQUEST)

                return Response({
                            'status': 'OK',
                            'message': 'Plan de trabajo creado exitosamente.',
                        }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'Error',
                    'message': 'Error en los datos del plan de trabajo.',
                    'errors': plan_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        user = self.request.user
       
        if(user != self.get_object().user):
            return Response({'mensaje': 'No tiene permisos para editar este plan de trabajo'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            plan_instance = self.get_object()
            plan_data = request.data.get('plan')
            actividades_data = request.data.get('actividades')
                
            proyecto_serializer = PlanTrabajoUpdateSerializer(data=plan_data)
            if proyecto_serializer.is_valid():
                plan = PlanTrabajoSerializer(instance=plan_instance, data=plan_data, partial=True)         
                if plan.is_valid():
                    plan.save()
            
            for actividad_data in actividades_data:
                if 'cumplimiento' in actividad_data and actividad_data['cumplimiento'] == True:
                    actividad_data['fecha_fin'] = datetime.now().strftime('%Y-%m-%d')
                elif 'cumplimiento' in actividad_data and actividad_data['cumplimiento'] == False:
                    actividad_data['fecha_fin'] = None
                    actividad_data['observaciones'] = None
                    
                actividad_serializer = ActividadUpdateSerializer(data=actividad_data)
                if actividad_serializer.is_valid():
                    actividad_instance = ActividadModel.objects.get(id_plan=plan_instance, id=actividad_data['id'])
                    actividad = ActividadSerializer(instance=actividad_instance, data=actividad_data, partial=True)       
                    if actividad.is_valid():
                        actividad.save()
            
            return Response({'mensaje': 'Plan de trabajo actualizado'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'mensaje': 'Error al actualizar el plan de trabajo', 'error': {str(e)}}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = request.user

        if instance.user != user:
            return Response({'mensaje': 'No tiene permisos para eliminar este plan de trabajo.'}, status=status.HTTP_403_FORBIDDEN)
        
        plantrabajo_id = instance.id
        PlanTrabajoModel.objects.filter(id=plantrabajo_id).delete()

        return Response({'mensaje': 'Plan de trabajo eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
