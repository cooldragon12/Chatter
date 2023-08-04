
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .encryption import Encryption
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'status', 'public_key', 'is_superuser']
        read_only_fields = ['id', 'username', 'status', 'public_key', 'is_superuser']


class RegisterSerializer(serializers.ModelSerializer):
    # REQUIRED PARAMETER
    username = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField( required=True, validators=[validate_password])
    password2 = serializers.CharField( required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'public_key']
        read_only_fields = ['id', 'public_key']
        write_only_fields = ['password', 'password2']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password does not match"})
        return attrs
    
    def create(self, validated_data):
        key = Encryption.createPrivateKeyRSA()
        try:
            user = User.objects.get(email=validated_data['email'])
        except User.DoesNotExist:
            user = User.objects.create(
                username = validated_data["username"],
                public_key = key.public_key(),
                private_key = key,
            )
            user.set_password(validated_data["password"])
            user.save()

        return user
        