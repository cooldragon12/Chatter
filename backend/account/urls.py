from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views


urlpatterns = [
    path('token/obtain/', TokenObtainPairView.as_view(),name ='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name =  'token_refresh'),
    # path('token/refresh/', TokenRefreshView.as_view(), name =  'token_refresh'),
    path('register/', RegisterView.as_view(), name = 'auth_register'),
]