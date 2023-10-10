
import stat
from sys import exception

from django.http import JsonResponse
from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import  GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from account import mixins
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth import  get_user_model
# Create your views here.

User = get_user_model()

class SessionView(APIView):
    permission_classes = (IsAuthenticated,)
    @staticmethod
    def get(request):
        return JsonResponse({"isAuhenicated": request.user.is_authenticated}, status=status.HTTP_200_OK)

class MeView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class AuthenticationView(mixins.AuthenticationMixins,GenericViewSet):
    permission_classes = (AllowAny,)

    def post(self, request):
        return self.login(request)

    def get(self, request):
        return self.logout(request)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer