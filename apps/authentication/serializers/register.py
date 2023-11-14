from django.contrib.auth.models import User
from apps.user.serializers.user import UserSerializer
from apps.user.models.information import UserInformationModel
from apps.user.serializers.information import InformationUserSerializer
from rest_framework import serializers

class RegisterUserSerializer(UserSerializer):
    email = serializers.EmailField(required=True)
    information = InformationUserSerializer()
    class Meta:
        model = User
        fields = ( 'id' ,'email', 'password', 'first_name', 'last_name', 'information')

    def create(self, validated_data):
        email = validated_data.get('email')
        information = validated_data.pop('information')
        user_instance, created = User.objects.get_or_create(username=email, defaults=validated_data)
        user_information, info_created = UserInformationModel.objects.get_or_create(user=user_instance, defaults=information)

        if not info_created:
            for key, value in information.items():
                setattr(user_information, key, value)
            user_information.save()
       
        self.context['user_created'] = user_instance
        return user_instance
    
    def validate_email(self, value):
        try: 
            User.objects.get(username=value)
        except User.DoesNotExist:
            return value        
        raise serializers.ValidationError({'username': 'This user already exists'})
        
    