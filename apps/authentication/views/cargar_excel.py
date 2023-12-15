from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.serializers.cargar_excel import RegisterExcelSerializer
from apps.authentication.serializers.token_pair import MyTokenObtainPairSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from apps.estadisticas.models.stats import UserStatsModel
import pandas as pd

#Registro
class RegisterExcelViewSet(ModelViewSet):
    http_method_names = ['post']
    authentication_classes = []
    permission_classes = [ AllowAny ]
    serializer_class = RegisterExcelSerializer
    parser_classes = [FileUploadParser]
    
    def create(self, request, *args, **kwargs):
        print(self.action)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            #print(f'🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈{'Entro al if'}🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')
            excel_file = request.data['file']
            excel_content = excel_file.read()
            df = pd.read_excel(excel_content, engine='openpyxl')

            self.create_users_from_excel(df)
            
            #serializer.save()
            return Response({'message': 'Usuarios registrados exitosamente'}, status=status.HTTP_201_CREATED)
        else:
            #print(f'🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈{'No entro al if'}🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')
            return Response({'mensaje': 'Mal', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def create_users_from_excel(self, df):
        for index, row in df.iterrows():
            email = row['email']
            identification = str(row['identification'])
            # Verificar si ya existe un usuario con el mismo email
            if User.objects.filter(username=email).exists():
                print(f'Usuario con email {email} ya existe. No se creará un duplicado.')
                continue

            # Verificar si ya existe un usuario con la misma identificación
            if UserInformationModel.objects.filter(identification=identification).exists():
                print(f'Usuario con identificación {identification} ya existe. No se creará un duplicado.')
                continue

            user_data = {
                'email': row['email'],
                'password': '1234',
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'information': {
                    'identification': str(row['identification']),
                    'user_type': "6"
                }
            }
            
            email = user_data['email']
            #print('🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')
            #print(email)
            information = user_data.pop('information', None)
            #print(user_data)
            #print(information)
            #print('🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈')

            user_instance, created = User.objects.get_or_create(username=email, defaults=user_data)
            user_information, info_created = UserInformationModel.objects.get_or_create(user=user_instance, defaults=information)
            stats_instance = UserStatsModel.objects.get_or_create(user=user_instance)

            if not info_created:
                for key, value in information.items():
                    setattr(user_information, key, value)
                user_information.save()

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer