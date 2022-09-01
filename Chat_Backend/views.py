
from django.shortcuts import get_object_or_404, get_list_or_404


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializer import RoomSerializer
from .models import Room,User, Message
from .mixins import JoinRoomMixin, LeaveRoomMixin



def get_user_rooms(user):
    usern = get_object_or_404(User, username=user)
    return get_list_or_404(Room, member = usern)
def check_code_exist(code):
    if Room.objects.filter(code = code).exists():
        return True
    return False
"""
NOTE: 
You can make a view using mixin to make it easy
"""



# Create your views here.
class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer(exclude_fields=['username', 'code','members', 'messages'])
    permission_classes = (IsAuthenticated,)
class RoomDetailsView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer(exclude_fields=['username'])
    permission_classes = (IsAuthenticated,)
    lookup_field = 'search_id'
    
class RoomCreateView(CreateAPIView):
    serializer_class = RoomSerializer(exclude_fields=['search_id', 'code', 'created_on', 'members', 'messages'])
    permission_classes = (IsAuthenticated,)

class RoomOperationView(viewsets.GenericViewSet, JoinRoomMixin, LeaveRoomMixin):
    serializer_class = RoomSerializer(exclude_fields=['search_id', 'code', 'created_on', 'members', 'messages','name', 'max_users','host'])
    permission_classes = (IsAuthenticated,)
    queryset = Room.objects.all()
    lookup_field = "code"
    