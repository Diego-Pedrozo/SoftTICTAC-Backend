from django.urls import reverse
from rest_framework import status
from apps.core.tests import APITestCaseCustom, AuthenticatedUser
from apps.user.choices import UserRanges

class TestLogin(APITestCaseCustom, AuthenticatedUser):
    active = True
    def test_can_user_login(self):
        self.print_title('inicio de sesion')
        
        self.create_user(UserRanges.CLIENT)
        
        data = {
            'username':'example@yopmail.com',
            'password':'@Mipassword123'
        }

        url=reverse('core:authentication:token_obtain_pair')
        
        response = self.client.post(url, data, format='json')
        self.custom_assert(
            response.status_code == status.HTTP_200_OK,
            f'El servidor responde con status OK. Estado: {response.status_code}',
            f'Falló la autenticacion del usuario. Estado: {response.status_code}',
            self.active
        )
        
        self.custom_assert(
            'access' in response.data,
            'Se retornó el token de acceso',
            'No se retornó el token de acceso',
            self.active
        )

        self.custom_assert(
            'refresh' in response.data,
            'Se retornó el token de refresco',
            'No se retornó el token de refresco',
            self.active
        )