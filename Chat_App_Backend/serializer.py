from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

from .models import Room, User, Message
def get_room(roomId):
    room = get_object_or_404(Room, id=roomId)
    return room
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'code', 'max_users', 'host', 'created_on')
        read_only_field = ('id', 'code')
class RoomUtilSerializer(serializers.ModelField):
    class Meta:
        model= Room
        fields = ('host', 'name', 'max_users')   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_field = ['id']
class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()
    user = serializers.CharField()
    timestamp = serializers.DateTimeField()
    
    def create(self, validated_data):
        user = User.objects.filter(username=validated_data["user"])[0]
        msg = Message.objects.create(
            user=user,
            content=validated_data["content"]
        )
        room = get_room(validated_data["room"])
        room.messages.add(msg)
    
    
    
class LoginSerializer(TokenObtainPairSerializer):
    
    
    # def get_token(cls, user):
    #     token = super().get_token(user)
        
    #     token['user'] = user.username
    #     # Returns the following in json:
    #     #  {
    #     #   username: <username>,
    #     #   token: <token>, 
    #     #   refresh_token: <refresh_token>
    #     #   }
    #     #
    #     return token
        
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        
        return data
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True, max_length=128)
    username = serializers.CharField(required=True, max_length=50)
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only= True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Pssword does not match"})
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
        