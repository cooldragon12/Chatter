
import stat
from sys import exception

from django.http import JsonResponse
from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from account import mixins
from .serializer import LoginSerializer, RegisterSerializer, UserSerializer
from .models import User
# Create your views here.

class SessionView(APIView):
    permission_classes = (IsAuthenticated,)
    @staticmethod
    def get(request):
        return JsonResponse({"isAuhenicated": request.user.is_authenticated}, status=status.HTTP_200_OK)

class MeView(APIView):
    permission_classes = (IsAuthenticated,)
    @staticmethod
    def get(request):
        return JsonResponse({"userinfo": request.user.username}, status=status.HTTP_200_OK)

class AuthenticationView(mixins.AuthenticationMixins,GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return self.login(request)

    def get(self, request):
        return self.logout(request)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer