from django.urls import path,re_path
from .views import RoomOperationView, RoomView, RoomCreateView, RoomDetailsView
from rest_framework_simplejwt.views import TokenRefreshView


""" URL Patterns for Backend
      parent url is 'api/'
"""

join_room = RoomOperationView.as_view({'put':'join'})
leave_room = RoomOperationView.as_view({'get':'leave'})

urlpatterns = [
   # Room  // GET
   path('room/<uuid:search_id>/', RoomDetailsView.as_view(), name='room_view'),
   path('room/', RoomView.as_view(), name='rooms'),
   # Create or Join // POST & PUT
   path('room/create-room/', RoomCreateView.as_view(),name="create_new_room"),
   re_path(r'room/join/(?P<code>[a-zA-Z0-9]{10})/?$', join_room, name="join_a_room"), 
   re_path(r'room/leave/(?P<code>[a-zA-Z0-9]{10})/?$', leave_room, name="leave_a_room"), 

]