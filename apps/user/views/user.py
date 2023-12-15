from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from apps.user.serializers.information import InformationUserSerializer, InformationUserUpdateSerializer
from apps.user.serializers.user import UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

# Usuarios CRUD
class UserViewSet(ModelViewSet):
    model = User
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated ]
    http_method_names = ['get', 'post', 'put', 'patch']
    
    def get_queryset(self):
        queryset = User.objects
        user_id = self.request.user.id
        queryset = queryset.exclude(id=user_id)
        
        return queryset
        
    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        user_data = request.data
        information_data = user_data.pop('information', None)

        user_instance = User.objects.get(pk=self.get_object().id)
        information_instance = UserInformationModel.objects.get(user=user_instance)

        user_serializer = UserUpdateSerializer(data=user_data)
        information_serializer = InformationUserUpdateSerializer(data=information_data)

        if user_serializer.is_valid(): 
            user = UserUpdateSerializer(instance=user_instance, data=user_data, partial=True)         
            if user.is_valid():
                user.save()
        else:
            return Response({'mensaje': 'Error en los datos del usuario', 'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        if information_serializer.is_valid():     
            information = InformationUserSerializer(instance=information_instance, data=information_data, partial=True)         
            if information.is_valid():
                information.save()
        else:
            return Response({'mensaje': 'Error en la información del usuario', 'error': information_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje': 'Usuario Actualizado'}, status=status.HTTP_200_OK)