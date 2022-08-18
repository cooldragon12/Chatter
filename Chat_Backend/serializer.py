from django.shortcuts import get_object_or_404

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist

from .models import Room, User, Message

def get_room(roomId):
    room = get_object_or_404(Room, id=roomId)
    return room
class RoomInfoSerializer(serializers.ModelSerializer):
    """Room Info"""
    class Meta:
        model = Room
        fields = ['id', 'name', 'code', 'host', 'created_on']
        
class SelfUserSerializer(serializers.ModelSerializer):
    members_in_room = RoomInfoSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'members_in_room']
        read_only_field = ['id']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RoomUtilSerializer(serializers.Serializer):
    """For Creating New Room"""
    host = SelfUserSerializer()
    name = serializers.CharField()
    max_users = serializers.IntegerField()
    
    
class RoomSerializer(serializers.ModelSerializer):
    """Full Detail in Room"""
    host = UserSerializer(many=False)
    members_in_room = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('id', 'name', 'code', 'max_users', 'host', 'created_on', 'members_in_room')
        read_only_field = ('id', 'code')


# MessageSerializer
class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()
    user = serializers.CharField()
    timestamp = serializers.DateTimeField()
    
    def create(self, validated_data):
        user = User.objects.filter(username=validated_data["user"])[0]
        msg = Message.objects.create(
            user=user,
            content=validated_data['content'],
            timestamp=validated_data['timestamp']
        )
        room = get_room(validated_data['roomId'])
        room.messages.add(msg)
class UserJoinSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=16)

    def update(self, validated_data):
        code = validated_data['code']
        user = get_object_or_404(User, username=validated_data['username'])
        room = get_object_or_404(Room, code=code)
        room.members.add(user)
        
        return {'detail':'Sucessfully joined'}
    def validate(self, attrs):
        
        if Room.objects.filter(members__username = attrs['username']).exists():
            raise serializers.ValidationError({'error':"You've already joined"})
        try:
            Room.objects.get(code=attrs['code'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error':"Room doesn't exist"})
        
        return attrs
# Suth Serializers 
# class LoginSerializer(TokenObtainPairSerializer):
        
#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data['user'] = SelfUserSerializer(self.user).data
#         data['access'] = str(refresh.access_token)

        
#         return data
# class RegisterSerializer(serializers.ModelSerializer):
#     # REQUIRED PARAMETER
#     email = serializers.EmailField(required=True, write_only=True, max_length=128)
#     username = serializers.CharField(required=True, max_length=50)
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only= True, required=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password', 'password2']
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({'password':"Password does not match"})
#         return attrs
#     def create(self, validated_data):
#         try:
#             user = User.objects.get(email=validated_data['email'])
#         except ObjectDoesNotExist:
#             user = User.objects.create(
#                 username = validated_data["username"],
#                 email = validated_data["email"],
#             )
#             user.set_password(validated_data["password"])
#             user.save()

#         return user
        