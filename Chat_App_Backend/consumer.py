from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .serializer import MessageSerializer
from .models import Message, User
from .views import get_10_messages
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' %self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data): # Recieve by the server
        data = self.text_to_json(text_data)
        # Directory of Commands
        self.commads[data['command']](self,data)


    # Sending Messages to the client
    def send_message(self, message): # send by server to client
        self.send(text_data=json.dumps(message)) 
    async def chat_message(self, e):
        # Send Directly to the other end
        message = e['message']
        await self.send(text_data=json.dumps(message))
    # Fetching the message from server
    def get_saved_messages(self,roomId):
        msgs = get_10_messages(roomId)
        msgs_list = []
        for i in msgs:
            msg_serialized = MessageSerializer(i)
            msgs_list.append(msg_serialized.data)
        return msgs_list

    def fetch_messages(self,data):
        
        msgs_list = self.get_saved_messages(data['roomId'])
        content = {
            'command': 'messages',
            'messages': msgs_list,
        }
        self.send_message(content)
    # New Message Save to database then back to user
    def new_message(self,data): # To save in database
        author = data["from"]
        new_msg = MessageSerializer()
        
        new_msg.create(
            user=author,
            content=data["content"],
            room = data["room"]
            )
        
        content = {
            'command' : 'new_message',
            'message' : new_msg.data
        }
        return self.send_new_message(content)
        

    async def send_new_message(self,message):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
        
    commads = {
        'messages':fetch_messages,
        'new_message':new_message,
    }
    
# class ChatConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['user']
#         self.room_group_name = 'chat_%s' %self.room_name

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
    
#     async def receive(self, text_data): # Recieve by the server
#         text_to_json = json.loads(text_data)
#         message = text_to_json['message']
#         user = text_to_json['user']
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': user,
#             }
#         )

#     async def chat_message(self, e): #
#         message = e['message']
#         user = e['user']
#         room = e['room']
#         await self.send_json({
#             'message':message,
#             'user':user,
#             'room':room
#         })