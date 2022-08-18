
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
from Chat_Backend.serializer import SelfUserSerializer
from .models import User

class LoginSerializer(TokenObtainPairSerializer):
        
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = SelfUserSerializer(self.user).data
        data['access'] = str(refresh.access_token)

        
        return data
class RegisterSerializer(serializers.ModelSerializer):
    # REQUIRED PARAMETER
    email = serializers.EmailField(required=True, write_only=True, max_length=128)
    username = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only= True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password does not match"})
        return attrs
    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create(
                username = validated_data["username"],
                email = validated_data["email"],
            )
            user.set_password(validated_data["password"])
            user.save()

        return user
        