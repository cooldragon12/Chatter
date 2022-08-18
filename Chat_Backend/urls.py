from django.urls import path
from .views import RoomJoinView, RoomView, RoomCreateView, RoomDetailsView
from rest_framework_simplejwt.views import TokenRefreshView


""" URL Patterns for Backend
      parent url is 'api/'
"""

urlpatterns = [
   # Room  // GET
   path('room/<uuid:search_id>/', RoomDetailsView.as_view(), name='room_view'),
   path('room/', RoomView.as_view(), name='rooms'),
   # Create or Join // POST & PUT
   path('room/create-room/', RoomCreateView.as_view(),name="create_new_room"),
   path('room/join/', RoomJoinView.as_view(), name="join_a_room"), 
   

]