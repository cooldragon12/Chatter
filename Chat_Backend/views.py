
from django.shortcuts import get_object_or_404, get_list_or_404


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializer import RegisterSerializer, RoomSerializer, UserJoinSerializer, UserSerializer, RoomUtilSerializer
from .models import Room,User, Message



def get_user_rooms(user):
    usern = get_object_or_404(User, username=user)
    return get_list_or_404(Room, member = usern)
def check_code_exist(code):
    if Room.objects.filter(code = code).exists():
        return True
    return False

# Create your views here.
class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
class RoomDetailsView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'search_id'
    
class RoomCreateView(APIView):
    serializer_class = RoomUtilSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, id=serializer.data.get('host'))
            room = Room(name=serializer.data.get('name'),host=user,max_users=serializer.data.get('max_users'))
            room.save()
            return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
class RoomJoinView(APIView):
    serializer_class = UserJoinSerializer
    permission_classes = (IsAuthenticated,)
    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.update(validated_data=serializer.data)
            return Response(data = response ,status=status.HTTP_202_ACCEPTED)
        return Response({'Bad Request': 'Invalid Code'}, status=status.HTTP_400_BAD_REQUEST)




    