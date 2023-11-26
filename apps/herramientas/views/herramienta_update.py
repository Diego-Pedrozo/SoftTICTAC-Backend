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
from rest_framework.response import Response
from datetime import date, datetime

class HerramientaUpdateViewSet(ModelViewSet):
    model = HerramientaModel
    serializer_class = HerramientaSerializer
    queryset =  HerramientaModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch', 'put']
    
    def update(self, request, *args, **kwargs):
        print(self.action)
        user = self.request.user
        
        if(user != self.get_object().user):
            return Response({'mensaje': 'No tiene permisos para editar esta herramienta'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if(self.get_object().estado == 'Pendiente'):
            return Response({'mensaje': 'La herramienta se encuentra en revisión'}, status=status.HTTP_401_UNAUTHORIZED)
            

        try:
            #instancias y datas
            herramienta_instance = self.get_object()
            herramienta_data = request.data.get('herramienta')
            tema_instance = TemaModel.objects.get(pk=herramienta_instance.id_tema.id)
            tema_data = request.data.get('tema')
            momentos_data = request.data.get('momentos')
            
            herramienda_serializer = HerramientaUpdateSerializer(data=herramienta_data)
            tema_serializer = TemaUpdateSerializer(data=tema_data)

            if herramienda_serializer.is_valid():
                #print('Herramienta valido')
                herramienta_instance.id_poblacion.clear()
                poblaciones_data = herramienta_data.get('id_poblacion', [])
                poblacion_ids = [poblacion['id'] for poblacion in poblaciones_data]
                herramienta_instance.id_poblacion.set(poblacion_ids)
                
                herramienta = HerramientaSerializer(instance=herramienta_instance, data=herramienta_data, partial=True)         
                if herramienta.is_valid():
                    herramienta.save()
            # else:
            #     return Response({'mensaje': 'Error en los datos de la herramienta', 'error': herramienda_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
            if tema_serializer.is_valid():
                #print('Tema valido')
                tema_instance.id_competencia.clear()
                competencias_data = tema_data.get('id_competencia', [])
                competencia_ids = [competencia['id'] for competencia in competencias_data]
                tema_instance.id_competencia.set(competencia_ids)
                
                tema = TemaSerializer(instance=tema_instance, data=tema_data, partial=True)            
                if tema.is_valid():
                    tema.save()
            # else:
            #     return Response({'mensaje': 'Error en los datos del tema', 'error': tema_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            for momento_data in momentos_data:
                momento_serializer = MomentoUpdateSerializer(data=momento_data)
                if momento_serializer.is_valid():
                    #print('Momento valido')
                    momento_instance = MomentoModel.objects.get(id_herramienta=herramienta_instance, nombre=momento_data['nombre'])
                    momento = MomentoSerializer(instance=momento_instance, data=momento_data, partial=True)       
                    if momento.is_valid():
                        momento.save()
                    
                    if momento_instance.nombre == 'Desarrollo':
                        procesos_data = momento_data.get("procesos", [])
                        procesos_ids_proporcionados = [proceso_data.get("id") for proceso_data in procesos_data]
                        procesos_a_eliminar = ProcesoModel.objects.filter(id_momento=momento_instance.id).exclude(id__in=procesos_ids_proporcionados)
                        procesos_a_eliminar.delete()

                        for proceso_data in procesos_data:
                            proceso_serializer = ProcesoUpdateSerializer(data=proceso_data)
                            
                            if proceso_serializer.is_valid():
                                #print('Proceso valido')
                                if 'id' not in proceso_data:
                                    #print('Nuevo')
                                    proceso_data['id_momento'] = momento_instance.id
                                    proceso = ProcesoSerializer(data=proceso_data)
                                else:
                                    proceso_instance = ProcesoModel.objects.get(id_momento=momento_instance.id, id=proceso_data["id"])
                                    if proceso_instance:
                                        #print('Existente')
                                        proceso = ProcesoUpdateSerializer(instance=proceso_instance, data=proceso_data, partial=True)
                                if proceso.is_valid():
                                    #print('Guardo')
                                    proceso.save()
                        
                # else:
                #     return Response({'mensaje': 'Error en los datos del momento', 'error': momento_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
            if herramienta_instance.estado not in ['Pendiente']:
                    #print('Pendiente')
                    herramienta_instance.estado = 'Pendiente'
                    herramienta_instance.fecha_aprobacion = None
                    herramienta_instance.save()

            return Response({'mensaje': 'Herramienta actualizada'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'mensaje': 'Error al actualizar la herramienta', 'error': {str(e)}}, 
                            status=status.HTTP_400_BAD_REQUEST)
    