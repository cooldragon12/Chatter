
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializer import MessageSerializer, RoomSerializer
from .models import Room,User, Message
from .mixins import JoinRoomMixin, LeaveRoomMixin



def get_user_rooms(user):
    usern = get_object_or_404(User, username=user)
    return get_list_or_404(Room, member = usern)
def check_code_exist(code):
    if Room.objects.filter(code = code).exists():
        return True
    return False
@action(detail=False,methods=['get'])
def ping(request):
    return Response({"message":"pong"}, status=status.HTTP_200_OK)
"""
NOTE: 
You can make a view using mixin to make it easy
"""

# Create your views here.

class RoomView(viewsets.GenericViewSet, RetrieveModelMixin,ListModelMixin, JoinRoomMixin, LeaveRoomMixin, CreateModelMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'search_id'
    lookup_field_code = "code"

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True,exclude_fields = ['username', 'code','members', 'messages'] )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={
            'max_users':request.data['max_users'],
            'name':request.data['name']
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        head = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=head)

