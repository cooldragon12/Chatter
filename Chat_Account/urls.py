from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginSerializerTokenView


urlpatterns = [
    path('token/obtain/', LoginSerializerTokenView.as_view(),name ='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name =  'token_refresh'),
    path('register/', RegisterView.as_view(), name = 'auth_register'),
]