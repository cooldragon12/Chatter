from django.urls import path
from .views import LoginSerializerTokenView, RegisterView, RoomView, RoomCreateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
   path('room/<str:room_name>', RoomView.as_view(), name='room_view'),
   path('auth/token/obtain/', LoginSerializerTokenView.as_view(),name ='token_obtain'),
   path('auth/token/refresh/', TokenRefreshView.as_view(), name =  'token_refresh'),
   path('register/', RegisterView.as_view(), name = 'auth_register'),
   path('create-room/', RoomCreateView.as_view(),name="create_new_room"),
   # path('join-room/<str:code>', join_room(),name='join_a_room'),
]