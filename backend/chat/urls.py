from django.urls import path,re_path
from .views import  RoomView,ping
from rest_framework_simplejwt.views import TokenRefreshView


""" URL Patterns for Backend
      parent url is 'api/'
"""

urlpatterns = [
   # Room  // GET
#    path('ping/', ping, name='ping'),
   re_path(r'^room/<uuid:search_id>/?$', RoomView.as_view({"get":"retrieve"}), name='room_view'),
   re_path(r'^room/?$', RoomView.as_view({"get":"list"}), name='room_all_rooms'),
   # Create or Join // POST & PUT
   re_path(r'^room/create/?$', RoomView.as_view({"post":"create"}),name="room_create"),
   re_path(r'^room/join/(?P<code>[a-zA-Z0-9]{10})/?$',RoomView.as_view({'post':'join'}), name="room_join"), 
   re_path(r'^room/leave/(?P<code>[a-zA-Z0-9]{10})/?$', RoomView.as_view({'post':'leave'}), name="room_leave"), 

]