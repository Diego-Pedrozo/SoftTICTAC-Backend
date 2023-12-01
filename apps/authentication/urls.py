from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.authentication.views.register import RegisterViewSet, EmailTokenObtainPairView
from apps.authentication.views.cargar_excel import RegisterExcelViewSet

app_name = "authentication"

SIMPLE_JWT_URLS = [
    # Otras rutas de la API
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', RegisterViewSet.as_view({'post':'create'}), name='register'),
    path('excel/', RegisterExcelViewSet.as_view({'post':'create'}), name='excel')
] + SIMPLE_JWT_URLS