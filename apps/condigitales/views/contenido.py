from rest_framework.viewsets import ModelViewSet
from apps.condigitales.models.contenido import ContenidoDigitalModel
from apps.condigitales.serializers.contenido import ContenidoDigitalSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.response import Response
from datetime import date, datetime

class ContenidoDigitalViewSet(ModelViewSet):
    model = ContenidoDigitalModel
    serializer_class = ContenidoDigitalSerializer
    queryset =  ContenidoDigitalModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    # def get_queryset(self):
    #     print(self.action)
    #     queryset = {
    #         'get': ContenidoDigitalModel.objects.all(),
    #         'partial_update': ContenidoDigitalModel.objects.filter(estado="Pendiente")
    #     }
    #     return queryset.get(self.action, super().get_queryset())
    
    def create(self, request, *args, **kwargs):
        print(self.action)
        user = self.request.user

        if 'user' not in request.data:
            request.data['user'] = user.id

        if 'fecha_creacion' not in request.data:
            request._full_data['fecha_creacion'] = datetime.now()

        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = self.request.user
        user_information = UserInformationModel.objects.get(user=user)

        if user_information.user_type not in ['2', '3']:
            return Response({'mensaje': 'No tiene permisos para cambiar el estado de este contenido.'}, status=status.HTTP_403_FORBIDDEN)

        if instance.estado == 'Pendiente' and user_information.user_type in ['2']:
            if request.data.get('estado') == 'Aprobado' and 'fecha_aprobacion' not in request.data:
                request.data['fecha_aprobacion'] = datetime.now()
            
            return super().partial_update(request, *args, **kwargs)
                
        elif instance.estado in ['Rechazado', 'Aprobado'] and user_information.user_type in ['2', '3']:
            request.data['estado'] = 'Pendiente'
            request.data['fecha_aprobacion'] = None
            return super().partial_update(request, *args, **kwargs)
            
    
    def list(self, request, *args, **kwargs):
        print(self.action)
        user = request.user
        estado = request.query_params.get('estado', None)
        user_information = UserInformationModel.objects.get(user=user)
         
        if estado == 'Pendiente' and user_information.user_type in ['2']:
            queryset = ContenidoDigitalModel.objects.filter(estado="Pendiente")

        elif estado == 'Rechazado' and user_information.user_type in ['2', '3']:
            queryset = ContenidoDigitalModel.objects.filter(estado="Rechazado", user=user)

        elif estado == 'Aprobado':
            queryset = ContenidoDigitalModel.objects.filter(estado="Aprobado")

        else:
            queryset = ""

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        user = request.user

        if instance.user != user:
            return Response({'mensaje': 'No tiene permisos para eliminar este contenido.'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)

    
    
    

    # @action(detail=False, methods=['post'], url_path='crear')
    # def crear(self, request):
    #     contenido_json = self.request.data

    #     if not contenido_json:
    #         return Response({'mensaje': 'No se envio ningun contenido'}, status=status.HTTP_400_BAD_REQUEST)
    #         #nombre = self.request.data.get('nombre')

    #     user_id = self.request.user.id
    #     user = User.objects.get(pk=user_id)
    #     contenido_nombre = contenido_json.get('nombre')
    #     contenido_url = contenido_json.get('url')
    #     contenido_visibilidad = contenido_json.get('visibilidad')
    #     contenido_linea = contenido_json.get('id_linea')
    #     contenido_descripcion = contenido_json.get('descripcion')
    #     contenido_poblacion = contenido_json.get('id_poblacion')
    #     contenido_imagenref = contenido_json.get('imagenReferencia')

    #     contenido = {'user': user.id, 'id_linea': contenido_linea, 'nombre': contenido_nombre, 
    #                  'url': contenido_url , 'visibilidad': contenido_visibilidad, 'descripcion': contenido_descripcion,
    #                  'id_poblacion': contenido_poblacion, 'imagen_ref': contenido_imagenref}
    #     contenido_serializer = ContenidoDigitalSerializer(data=contenido)

    #     if contenido_serializer.is_valid():
    #         contenido = contenido_serializer.save()
        
    #     else:
    #         return Response(contenido_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     return Response({'mensaje': 'Contenido creado'}, status=status.HTTP_200_OK)
    
    # @action(detail=False, methods=['get'], url_path='contenidos-pendientes')
    # def contenidos_pendientes_lider_ppt(self, request):
    #     user = self.request.user
    #     try:
    #         user_information = UserInformationModel.objects.get(user=user)
    #     except UserInformationModel.DoesNotExist:
    #         return Response({'mensaje': 'El usuario no tiene información asociada.'}, status=status.HTTP_404_NOT_FOUND)

    #     if user_information.user_type not in ['2']:
    #         return Response({'mensaje': 'No tiene permisos para acceder a estos contenidos.'}, status=status.HTTP_403_FORBIDDEN)

    #     contenidos_pendientes = ContenidoDigitalModel.objects.filter(estado='Pendiente')
    #     serializer = ContenidoDigitalSerializer(contenidos_pendientes, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @action(detail=False, methods=['get'], url_path='contenidos-rechazados')
    # def contenidos_rechazados_docente(self, request):
    #     user = self.request.user
    #     try:
    #         user_information = UserInformationModel.objects.get(user=user)
    #     except UserInformationModel.DoesNotExist:
    #         return Response({'mensaje': 'El usuario no tiene información asociada.'}, status=status.HTTP_404_NOT_FOUND)

    #     if user_information.user_type not in ['2', '3']:
    #         return Response({'mensaje': 'No tiene permisos para acceder a estos contenidos.'}, status=status.HTTP_403_FORBIDDEN)

    #     contenidos_rechazados = ContenidoDigitalModel.objects.filter(estado='Rechazado', user=user)
    #     serializer = ContenidoDigitalSerializer(contenidos_rechazados, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # @action(detail=False, methods=['put'], url_path='actualizar-estado')
    # def actualizar_estado_contenido(self, request):
    #     data = self.request.data
    #     user = self.request.user
    #     user_information = UserInformationModel.objects.get(user=user)
    #     if user_information.user_type not in ['2']:
    #         return Response({'mensaje': 'No tiene permisos para cambiar el estado de este contenido.'}, status=status.HTTP_403_FORBIDDEN)

    #     contenido = ContenidoDigitalModel.objects.get(pk=data.get('id_contenido'))
    #     contenido.estado = data.get('estado')
    #     contenido.recomendacion = data.get('recomendacion')
    #     contenido.fecha_aprobacion = datetime.now()
    #     contenido.save(update_fields=['estado', 'recomendacion', 'fecha_aprobacion'])

    #     serializer = ContenidoDigitalSerializer(contenido)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    
