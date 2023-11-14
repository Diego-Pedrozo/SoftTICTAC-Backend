from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.authentication.serializers.register import RegisterUserSerializer
from apps.authentication.serializers.token_pair import MyTokenObtainPairSerializer

#Registro
class RegisterViewSet(ModelViewSet):
    http_method_names = ['post']
    authentication_classes = []
    permission_classes = [ AllowAny ]
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user_instance = serializer.context.get('user_created')
        refresh = RefreshToken.for_user(user_instance)
        response_data = {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }           
        
        return Response(response_data, status=201)

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer