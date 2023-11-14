from apps.user.models.information import UserInformationModel
from rest_framework import serializers

#More information for user model
class InformationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['identification']
