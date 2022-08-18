from django.urls import path,re_path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    # path('/chat/<str:room_name>', ChatConsumer.as_asgi()),

]