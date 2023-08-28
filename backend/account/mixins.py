from rest_framework import status, exceptions
from django.http import JsonResponse
from django.contrib.auth import login as _login, logout as _logout, authenticate
from account.serializer import LoginSerializer


class AuthenticationMixins:
    def login(self,request):
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
            _login(request, user)
            # Return user info
            print("login success")
            return JsonResponse({"userinfo": serializer.data}, status=status.HTTP_200_OK)
        except exceptions.ValidationError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": 'Sorry, there is a problem in the server'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def logout(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=status.HTTP_400_BAD_REQUEST)

        _logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})