from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    """ User Model

    Inhireted AbstractUser with addtional parameter for userid.
    """
    STATUS_CHOICES = [('online', 'STATUS_ONLINE'), ('offline','STATUS_OFFLINE')]
    id = models.CharField(unique=True, max_length=16,default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=128)
    username = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=20)
    status = models.CharField(null=False, choices=STATUS_CHOICES, max_length=10, default=STATUS_CHOICES[1])
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    @classmethod
    def get_number_user(self) -> int:
        pass
    def __str__(self) -> str:
        return str(self.username)
    
    # def get_user_by_id(id):
    #     user = User.objects.filter(id=id)