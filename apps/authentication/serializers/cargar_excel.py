from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from apps.user.serializers.user import UserSerializer
from apps.user.models.information import UserInformationModel
from apps.user.serializers.information import InformationUserSerializer
from rest_framework import serializers
import pandas as pd

class RegisterExcelSerializer(UserSerializer):
    #email = serializers.EmailField(required=True)
    #information = InformationUserSerializer()
    excel = serializers.FileField(required=False)

    class Meta:
        model = User
        fields = ['excel']

    # def create(self, validated_data):
    #     try:
    #         if 'excel' in validated_data:
    #             print(f'🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈{'Entro al if'}🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')
    #             archivo = validated_data.pop('excel')
    #             df = pd.read_excel(archivo)
    #             user_instances = []

    #             for index, row in df.iterrows():
    #                 user_data = {
    #                     'email': row['email'],
    #                     'password': row['password'],
    #                     'first_name': row['first_name'],
    #                     'last_name': row['last_name'],
    #                     'information': {
    #                         'identification': row['identification'],
    #                         'user_type': "3"
    #                     }
    #                 }
    #                 email = user_data.get('email')
    #                 information = user_data.get('information')
    #                 user_instance, created = User.objects.get_or_create(username=email, defaults=information)
    #                 user_information, info_created = UserInformationModel.objects.get_or_create(user=user_instance, defaults=information)

    #                 if not info_created:
    #                     for key, value in information.items():
    #                         setattr(user_information, key, value)
    #                     user_information.save()
                        
    #                 user_instances.append(user_instance)

    #             return user_instances
            
    #         else:
    #             print(f'🎈🎈🎈🎈🎈{'No jijijaja'}🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')
    #             return None
    #     except Exception as e:
    #         return Response({'error': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)   
            
        
    # def register_users_from_excel(self, archivo):
    #     print(f'🎈🎈🎈🎈🎈{'Entro a register excel'}')
    #     df = pd.read_excel(archivo)

    #     for index, row in df.iterrows():
    #         user_data = {
    #             'email': row['email'],
    #             'password': row['password'],
    #             'first_name': row['first_name'],
    #             'last_name': row['last_name'],
    #             'information': {
    #                 'identification': row['identification'],
    #                 'user_type': "3"
    #             }
    #         }
    #         self.create(user_data)


    def validate_email(self, value):
        try: 
            User.objects.get(username=value)
        except User.DoesNotExist:
            return value        
        raise serializers.ValidationError({'username': 'Ya existe un usuario con ese email'})
        
    