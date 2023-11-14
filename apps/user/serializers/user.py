from rest_framework import serializers
from django.contrib.auth.models import User
from apps.user.serializers.information import InformationUserSerializer


class UserSerializer(serializers.ModelSerializer):
    information = InformationUserSerializer()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','information', 'username', 'first_name','last_name', 'email', 'is_active', 'password']
    
    def create(self, validated_data):
        information_serializer = InformationUserSerializer(data=validated_data["information"])
        
        if information_serializer.is_valid():
            information_serializer.save()
            validated_data["information"] = information_serializer.instance
            user_instance = super().create(validated_data)
            information_serializer.instance.user = user_instance
            information_serializer.instance.save()
        return user_instance

    def update(self, instance, validated_data):
        information_data = validated_data.pop('information', None)

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        if information_data:
            information_serializer = InformationUserSerializer(instance.information, data=information_data, partial=True)
            if information_serializer.is_valid():
                information_serializer.save()

        return instance
