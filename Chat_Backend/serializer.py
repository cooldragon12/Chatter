from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Room, User, Message

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
    
    # Need a little imporvement here
    # The validated_data cannot find
    def do_join(self,instance,user):
        self.join(instance,user)
    def do_leave(self, instance,user):
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
    # rooms = RoomSerializer(exlude_fields=['host', 'messages', 'username'])
    class Meta:
        model = User
        fields = ['username', 'is_active','email', 'date_joined','status','is_active']
class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()
    user = serializers.CharField()
    timestamp = serializers.DateTimeField()
    # Create new Message
    def create(self, validated_data):
        user = User.objects.filter(username=validated_data["user"])[0]
        msg = Message.objects.create(
            user=user,
            content=validated_data['content'],
            timestamp=validated_data['timestamp']
        )
        room = get_room(validated_data['roomId'])
        room.messages.add(msg)
    # And get the messages

class RoomSerializer(BaseModelSerializer,UserOperation):
    """General Room Serializer
    
    NOTE: 
    To Remove other fields, in intialization in the parameter just put `exlude_fields` 
    then enter the string of the variable in the list.
    """

    host = UserSerializer(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    username = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Room
        fields =  ['search_id', 'host','name', 'max_users', 'code', 'created_on', 'members','messages','username']
    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data.get('host'))
        room = Room(name=validated_data.get('name'),host=user,max_users=validated_data.get('max_users'))
        room.members.add(user)
        room.save()


    
# MessageSerializer


    # def validate(self, attrs):
    #     # if Room.objects.filter(members__username = attrs['username']).exists():
    #     #     raise serializers.ValidationError({'error':"You've already joined"})
    #     # try:
    #     #     Room.objects.get(code=attrs['code'])
    #     # except ObjectDoesNotExist:
    #     #     raise serializers.ValidationError({'error':"Room doesn't exist"})
    #     return attrs

        # return attrs
    
