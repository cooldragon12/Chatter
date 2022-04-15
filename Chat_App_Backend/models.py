
from django.db import models
from django.contrib.auth.models import AbstractUser
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

def generate_unique_id():
    """ Generate Unique Id
    
    Generate random id from hexadecimal with maximum of 10 characters. 
    """
    length = 10
    while True:
        ids = ''.join(random.choices(string.hexdigits, k=length))
        if User.objects.filter(id=ids).count() == 0:
            break
        break
    return ids
# Create your models here.
class User(AbstractUser):
    """ User Model

    Inhireted AbstractUser with addtional parameter for userid.
    """
    id = models.CharField(unique=True, max_length=16,default=generate_unique_id, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=128)
    username = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=20)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    @staticmethod
    def get_number_user() -> int:
        return User.objects.all().count()
    def __str__(self) -> str:
        return str(self.username)
    
    # def get_user_by_id(id):
    #     user = User.objects.filter(id=id)

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(to=User, related_name='author_message', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    """ Room Model
    
    Model of room to chat in and join in.
    """
    # Room Details
    code = models.CharField(unique=True, max_length=16, default=generate_secret_code, editable=False)
    name = models.CharField(max_length=100)
    max_users = models.IntegerField(blank=True)
    host = models.OneToOneField(User,on_delete=models.CASCADE, related_name="User_id")
    created_on =  models.DateTimeField(auto_now_add=True)
    # Room 
    member = models.ManyToManyField(User, blank=True, related_name="member_in_room")
    messages = models.ManyToManyField(Message, blank=True)
    def __str__(self):
        self.name
    def change_room_name(self, newName):
        self.name = newName
        self.save()
    def change_max_users(self, number):
        self.max_users= number
        self.save()

    
    
    


