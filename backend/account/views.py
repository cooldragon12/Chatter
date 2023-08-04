
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import RegisterSerializer
from .models import User
# Create your views here.
# class ObtainCookieTokenView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
        
#         response.set_cookie(
#             key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
#             expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
#             value=response.data['refresh'],
#             # secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#             httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#             # samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
#             # domain=settings.ALLOWED_HOSTS[2],
#             path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH']
#         )
#         response.set_cookie(
#             key=settings.SIMPLE_JWT['AUTH_COOKIE_ACCESS'],
#             expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
#             value=response.data['access'],
#             # secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#             httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#             # samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
#             # domain=settings.ALLOWED_HOSTS[2],
#             path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH']
#         )
#         return response
# class RefreshCookieTokenView(TokenRefreshView):
#     permission_classes = (AllowAny,)
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data={"refresh":request.COOKIES.get('__refresh')})
#         try:
#             serializer.is_valid(raise_exception=True)
#         except TokenError as e:
#             raise InvalidToken(e.args[0])

#         response = Response(serializer.validated_data, status=status.HTTP_200_OK)  
#         response.set_cookie(
#             key=settings.SIMPLE_JWT['AUTH_COOKIE_ACCESS'],
#             expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
#             value=response.data['access'],
#             # secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#             httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#             # samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
#             # domain=settings.ALLOWED_HOSTS[2],
#             path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH']
#         )
#         return response
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class = RegisterSerializer