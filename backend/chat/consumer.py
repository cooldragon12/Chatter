
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializer import MessageSerializer, UserSerializer
from .models import Message, Room
from account.models import User

def get_user(user_id):
    return get_object_or_404(User, id=user_id)

class ChatConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name:str = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat-{self.room_name}'
        self.user = self.scope['user']
        # check if the room exist
        await self.get_room(self.room_name)
        # Join room group / More like connecting to the group
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # await self.update_user_online(self.user)
        await self.accept()
        # Send the room name to the client
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type':'message.fetch','roomId':self.room_name}
        )
    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # status update if the user
        # await self.update_user_offline(self.user)
    async def get_room(self, room_name):
        try:
            return await database_sync_to_async(Room.objects.get)(name=room_name)
        except Room.DoesNotExist:
            await self.close(code=404)
    # Recieves event from client
    async def receive_json(self, content, **kwargs): # Recieve by the server
        # Directory of Commands
        print(content["type"])
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':content['type'],
                'roomId':self.room_name,
                'content':content
            }
        )
    
    # Methods/ types available============================================

    # Fetching the message from server
    async def message_fetch(self, data:dict):
        """Fetching the messages of the group""" 
        print("Fetching......")
        msgs = await self.get_10_messages(data['roomId'])
        msg_serialized = MessageSerializer(msgs, many=True)
        await self.send_json({
            'type': 'message.fetch',
            'messages': msg_serialized.data,
            'status':'delivered'
        })
    async def room(self):

        print(self.room_name)
        await self.send_json({
            'type':'room.echo',
            'room':self.room_name

        })
    # New Message Save to database then back to user ========================
    async def message_new(self, data:dict): # To save in database
        # Parsing the data then send message to group layer
        """Parsing the new messege"""
        print("New Message")
        new_msg = MessageSerializer(data={
            'user':self.user.id,
            'content':data["content"],
            'room':data["roomId"]
        })
        new_msg.is_valid(raise_exception=True)
        new_msg.save()
        # database_sync_to_async(new_msg.create(new_msg.data))
        await self.send_json({
            'type':'message.new',
            'message':new_msg.data
        })
    # Triggers when the user joined
    async def new_user_joined(self,data):
        await self.send_json({
            'type':'chat.new_user',
            'message': data['user']+' has joined the conversation'
        })
    
    async def user_leave(self,data):
        await self.send_json({
            'type':'chat.user_leave',
            'message': data['user']+' leave the conversation'
        })

    @database_sync_to_async
    def update_user_online(self, user):
        return User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[0])

    @database_sync_to_async
    def update_user_offline(self, user):
        return User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[1])
    
    @database_sync_to_async
    def get_10_messages(self,roomId):
        room = get_object_or_404(Room, search_id=roomId)
        return room.messages.order_by("-timestamp").all()[:10]  

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    pass