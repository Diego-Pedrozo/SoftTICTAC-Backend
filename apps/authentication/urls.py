from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.authentication.views.register import RegisterViewSet, EmailTokenObtainPairView
app_name = "authentication"

SIMPLE_JWT_URLS = [
    # Otras rutas de la API
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post':'create'}), name='register')
] + SIMPLE_JWT_URLS