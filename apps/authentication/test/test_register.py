from rest_framework import status
from apps.core.tests import APITestCaseCustom
from django.urls import reverse
from django.contrib.auth.models import User

class TestRegister(APITestCaseCustom):
    active = True
    def test_can_register_user(self):
        self.print_title('Registro de usuario')
        data = {
                "email": "example@yopmail.com",
                "password": "@Mipassword123",
                "username": "example",
                "first_name": "Vendedor",
                "last_name": "Ventas",
                "information":{
                    "city": "Paris",
                    "country": "Francia",
                    "phone": "9999999999"
                }
            }
        
        url = reverse('core:authentication:register')
        response = self.client.post(url, data, format='json')
        
        self.custom_assert(
            response.status_code == status.HTTP_201_CREATED,
            f'Se creó el usuario. Estado: {response.status_code}',
            f'No se creó el usuario. Estado: {response.status_code}',
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
        

        self.custom_assert(
            User.objects.filter(username='example').exists(),
            f"El usuario {data['username']} se creó",
            f"El usuario {data['username']} no se creó",
            self.active
        )
        
