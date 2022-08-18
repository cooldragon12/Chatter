
import uuid
from django.db import models
from Chat_Account.models import User
# from django.utils.translation import ungettext_lazy as _
import random
import string
''' Models 
Consist:
    Room Model
    User Model
'''
def generate_secret_code():
    """ Generate Secret Code
    
    Generate random code from ascii in lower case.
    """
    length = 16

    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(to=User, related_name='author_message', on_delete=models.CASCADE, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def edit_message(self, new_message):
        self.content = new_message
        self.save()
class Room(models.Model):
    """ Room Model
    
    Model of room to chat in and join in.
    """
    search_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    # Room Details
    name = models.CharField(max_length=100)
    max_users = models.IntegerField(blank=True)
    host = models.ForeignKey(User,on_delete=models.CASCADE, related_name="User_id")
    # Not Editable
    code = models.CharField(unique=True, max_length=16, default=generate_secret_code, editable=False)
    created_on =  models.DateTimeField(auto_now_add=True)
    # Room 
    members = models.ManyToManyField(User, blank=True, related_name="members_in_room")
    messages = models.ManyToManyField(Message, blank=True)
    def __str__(self):
        return self.name
    def change_room_name(self, newName):
        self.name = newName
        self.save()
    def change_max_users(self, number):
        self.max_users= number
        self.save()

    
    
    


