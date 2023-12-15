from django.urls import path, include
from rest_framework import routers
from apps.user.views.user import UserViewSet
from apps.user.views.user_list import UserListViewSet 

app_name='user'

router = routers.DefaultRouter()
#router.register(viewset=UserViewSet, basename='user', prefix='')
#router.register(viewset=UserListViewSet, basename='userlist', prefix='userlist')

urlpatterns = [path('', include(router.urls))]
