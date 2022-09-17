
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializer import MessageSerializer, UserSerializer
from .models import Message, Room
from Chat_Account.models import User
"""
NOTE: Can't connect to the socket


"""
def get_user(user_id):
    return get_object_or_404(User, id=user_id)

class ChatConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat-{self.room_name}'
        self.user = self.scope['user']
        # Join room group / More like connecting to the group
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        print(self.channel_name)
        print('created a group')
        # await self.update_user_online(self.user)
    
        await self.accept()
    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        # status update if the user
        await self.update_user_offline(self.user)
    
    # Message Related =================================================
    async def receive_json(self, content, **kwargs): # Recieve by the server
        # Directory of Commands
        await self.channel_layer.group_send(self.room_group_name, content)
        await self.commands[content['command']](self,content)

    # Sending Messages to the client
    async def send_message(self, message): # send by server to client
        await self.send_json(content=message)

    # Fetching the message from server
    async def fetch_messages(self, data:dict):
        """Fetching the messages of the group""" 
        msgs = await self.get_10_messages(data['roomId'])
        msgs_list = []
        for i in msgs:
            msg_serialized = MessageSerializer(i)
            msgs_list.append(msg_serialized.data)
        content = {
            'command': 'messages',
            'messages': msgs_list,
        }
        self.send_message(content)

    
    # New Message Save to database then back to user ========================
    def new_message(self, data:dict): # To save in database
        # Parsing the data then send message to group layer
        """Parsing the new messege"""

        
        new_msg = MessageSerializer(data={
            'user':self.user.id,
            'content':data["content"],
            'room':data["roomId"]
        }, exclude_fields=['timestamp'])
        new_msg.is_valid()
        
        # database_sync_to_async(new_msg.create(new_msg.data))
        
        return self.send_message(new_msg.data)
        

    # async def send_new_message(self,message):
    #     print("sent")
    #     await self.send_message()
      
    @database_sync_to_async
    def update_user_online(self, user):
        return User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[0])

    @database_sync_to_async
    def update_user_offline(self, user):
        return User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[1])
    
    commands = {
        'messages':fetch_messages,
        'new_message':new_message,
    }
    @database_sync_to_async
    def get_10_messages(self,roomId):
        room = get_object_or_404(Room, search_id=roomId)
        return room.messages.order_by("-timestamp").all()[:10]  
