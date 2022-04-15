from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,UpdateAPIView,CreateAPIView
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializer import RegisterSerializer, RoomSerializer, UserSerializer, LoginSerializer, RoomUtilSerializer
from .models import Room,User, Message


def get_10_messages(roomId):
    room = get_object_or_404(Room, id=roomId)
    return room.messages.order_by("-timestamp").all()[:10]

def get_user_rooms(user):
    usern = get_object_or_404(User, username=user)
    return get_object_or_404(Room, member = usern)
# Create your views here.
class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)
class RoomDetailsView(RetrieveAPIView):
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated)
    def get_queryset(self):
        queryset = None
        username = self.request.query_params.get('username', None)
        if username is not None:
            rooms = get_user_rooms(username)
            queryset = rooms.name.all()
        return queryset
class RoomCreateView(APIView):
    serializer_class = RoomUtilSerializer
    permission_classes = (IsAuthenticated)
    def post(self, request, format=None):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, username=serializer.data.username)
            room = Room(name=serializer.data.name,host=user,max_users=serializer.data.max_users)
            room.save()
            return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
# def join_room(request, code):
#     if request.method == 'POST':
#         user = get_object_or_404(User, username = request['username'])
#         room = get_object_or_404(Room, code=code)
#         room.member.add(user)
#     return



# class UserViewSet(viewsets.ModelViewSet):
#     http_method_names =['get']
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated)
#     filter_backends = [filters.OrderingFilter]
#     ordering = ['-updated']
#     def get_object(self):
#         lookup_field_value = self.kwargs[self.lookup_field]

#         obj = User.objects.get(lookup_field_value)
#         self.check_object_permissions(self.request, obj)

#         return obj

class LoginSerializerTokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer

    