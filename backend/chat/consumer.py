
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.exceptions import ValidationError
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
        # self.user = self.scope['user']
        # check if the room exist
        self.room = await self.get_room(self.room_name)
        # Join room group / More like connecting to the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        # await self.update_user_online(self.user)
        # Send the room name to the client
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type':'ping'}
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
            room = await database_sync_to_async(Room.objects.get)(name=room_name)
            return room
        except Room.DoesNotExist:
            await self.close(code=404)
    # Recieves event from client
    async def receive_json(self, content, **kwargs): # Recieve by the server
        # Directory of Commands
        try:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':content['type'],
                    'room_id':self.room.id,
                    'content':content['message']
                }
            )
        except Exception as e:
            print(e)
    
    # Methods/ types available============================================

    # Fetching the message from server
    async def message_fetch(self, data):
        """Fetching the messages of the group""" 
        print("Fetching......")
        msgs = await database_sync_to_async(self.room.messages.order_by("-timestamp").all)()
        if msgs is None:
            await self.send_json({
                'type': 'message.fetch',
                'messages': [],
                'status':'delivered'
            })
            return
        msg_serialized = MessageSerializer(msgs, many=True)
        
        await self.send_json({
            'type': 'message.fetch',
            'messages': msg_serialized.data,
            'status':'delivered'
        })
    # Ping Pong ===========================================================
    async def ping(self, data):
        await self.send_json({
            'type':'pong',
            'message':"Connected to "+self.room_name,
            'status':'delivered'
        })
    # New Message Save to database then back to user ========================
    async def message_new(self, data): # To save in database
        # Parsing the data then send message to group layer
        """Parsing the new messege"""
        # print("New Message")
        try:
            new_msg = MessageSerializer(data={
                'user':1,
                'encrypted_content':data["content"],
                'conversation':data["room_id"]
            })
            # print("Instance created")
            await database_sync_to_async(new_msg.is_valid)(raise_exception=True)
            # print("Validated")
            # print("Saving to database")
            await database_sync_to_async(new_msg.save)()
            # print("Saved")
            # print(new_msg.data)
            await self.send_json({
                'type':'message.new',
                'message':new_msg.data
            })
        except Exception as e:
            await self.send_json({
                'type':'message.new',
                'status':'error',
                'message':e
            })
    async def message_seen(self, data):
        """Update the message status to seen"""
        try:
            msg = await database_sync_to_async(Message.objects.get)(id=data['message_id'])
            await database_sync_to_async(msg.statusChange)("read")
            await self.send_json({
                'type':'message.seen',
                'message':msg.id
            })
        except Exception as e:
            await self.send_json({
                'type':'message.seen',
                'status':'error',
                'message':e
            })
    async def message_received(self, data):
        """Update the message status to received"""
        try:
            msg = await database_sync_to_async(Message.objects.get)(id=data['message_id'])
            await database_sync_to_async(msg.statusChange)("received")
            await self.send_json({
                'type':'message.received',
                'message':msg.id
            })
        except Exception as e:
            await self.send_json({
                'type':'message.received',
                'status':'error',
                'message':e
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

   
async def update_user_online( user):
    return await database_sync_to_async(User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[0]))

async def update_user_offline(user):
    return await database_sync_to_async(User.objects.filter(pk=user.pk).update(status=User.STATUS_CHOICES[1]))
    

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    pass