
import stat
from sys import exception
from django.contrib.auth import login, logout

from django.http import JsonResponse
from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
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

class AuthenticationView(GenericAPIView):
    permission_classes = (AllowAny,)

    def _login(request):
        try:
            # Check if username and password is provided
            if request.data["username"] == "" or request.data["password"] == "":
                return exceptions.ValidationError('Please provide username and password')
        
            # Check if user is already logged in
            if request.user.is_authenticated:
                return exceptions.ValidationError('You\'re already logged in.')
            
            serializer = LoginSerializer(data=request.data)
            # Check if username and password is valid
            serializer.is_valid()
            user = serializer.validated_data
            # Login user
            login(request, user)
            # Return user info
            return JsonResponse({"userinfo": user}, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def _logout(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=status.HTTP_400_BAD_REQUEST)

        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer