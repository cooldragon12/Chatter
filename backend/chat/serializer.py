from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Room, Message
from account.encryption import Encryption

User = get_user_model()

def get_room(roomId):
    room = get_object_or_404(Room, id=roomId)
    return room

class UserOperation:
    """
        Operation of User in the room
    """
    def join(self, instance, validated_data):
        user = get_object_or_404(User, username=validated_data)
        instance.members.add(user)
        instance.save()
        
        return instance
    def leave(self, instance, validated_data):
        user = get_object_or_404(User, username=validated_data)
        instance.members.remove(user)
        instance.save()
        return instance
    
    # Authority
    def remove(self, instance, validated_data):
        user = get_object_or_404(User, username=validated_data)
        instance.members.remove(user)
        instance.save()
        return instance
    # Need a little imporvement here
    # The validated_data cannot find
    def do_join(self,instance,user):
        self.join(instance,user)
    def do_leave(self,instance,user):
        self.leave(instance, user)

class BaseModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)
        # include_only_fields = kwargs.pop('include_only_fields', None)
        super(BaseModelSerializer, self).__init__(*args, **kwargs)

        if exclude_fields:
            # to remove some other fields that been indicated
            for field_name in exclude_fields:
                self.fields.pop(field_name)
    
class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'public_key']
        
class MessageSerializer(BaseModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['timestamp']

    def validate(self, attrs):
        if attrs['encrypted_content'] == '':
            raise serializers.ValidationError({'error':"Message cannot be empty"})
        # Encryption of the message in the databse
        attrs['encrypted_content'] = Encryption(privateKey=attrs['conversation'].host.private_key).encryptRSA(attrs['encrypted_content'], attrs['receiver'].public_key)
        return 
    
    

class RoomSerializer(BaseModelSerializer,UserOperation):
    """General Room Serializer
    
    NOTE: 
    To Remove other fields, in intialization in the parameter just put `exlude_fields` 
    then enter the string of the variable in the list.
    """
    # messages = MessageSerializer()
    class Meta:
        model = Room
        fields =  ['search_id', 'host','name', 'max_users', 'code', 'created_on', 'members', 'messages']
        read_only_fields =[
            'search_id',
            'code',
            'created_on',
            'messages',
            'members'
        ]

    def validate(self, attrs):
        if Room.objects.filter(members__pk = attrs['username']).exists():
            raise serializers.ValidationError({'error':"You've already joined"})
        try:
            Room.objects.get(code=attrs['code'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'error':"Room doesn't exist"})
        return attrs
    

