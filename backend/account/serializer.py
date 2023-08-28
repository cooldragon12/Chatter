
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .encryption import Encryption
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'status', 'public_key', 'is_superuser']
        read_only_fields = ['id', 'username', 'status', 'public_key', 'is_superuser']

class LoginSerializer(serializers.Serializer):
    username_field = get_user_model().USERNAME_FIELD
    password = serializers.CharField(required=True, max_length=50, write_only=True)

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError({'account':"Account does not exist or Password is incorrect"})
        return user


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
        