from apps.user.models.information import UserInformationModel
from rest_framework import serializers

#More information for user model
class InformationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['identification', 'user_type']

class InformationUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['identification', 'user_type', 'user']

class InformationUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['user_type']