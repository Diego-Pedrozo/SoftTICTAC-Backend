from django.urls import path, include
from rest_framework import routers
from apps.user.views.user import UserViewSet 

app_name='user'

router = routers.DefaultRouter()
router.register(viewset=UserViewSet, basename='user', prefix='')

urlpatterns = [path('', include(router.urls))]
