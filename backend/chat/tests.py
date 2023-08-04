from django.test import TestCase
from .models import Room, User
from django.shortcuts import get_object_or_404
# Create your tests here.
class RoomTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email='johndelencabo@gmail.com', username='cooldragon12', password='johntemots')
        Room.objects.create(code='00000',name="ThisIsMe",max_users=6,host=user)
        self.currentRoom = get_object_or_404(Room, name='00000')
    def changing_name_case(self):
        newName = 'NewTry'
        self.currentRoom.change_room_name(newName)
        self.assertEqual(self.currentRoom.name, newName)
    def changing_maxusers_case(self):
        self.currentRoom.change_max_users(8)
        self.assertEqual(self.currentRoom.max_users, 8)
        
