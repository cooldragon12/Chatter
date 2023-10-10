from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .encryption import Encryption

import random
import string
# Manager for User
class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        private_key = Encryption.createPrivateKeyRSA(512)
        serilized_private_key = Encryption(privateKey=private_key)
        user = self.model(private_key=serilized_private_key.serializePrivateKey(), public_key=serilized_private_key.serializePublicKey(),
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(password, **extra_fields)


def generate_id(length=16):
    """ Generate Secret Code
    
    Generate random code from ascii in lower case.
    """
    length = length

    while True:
        code = ''.join(random.choices(string.hexdigits, k=length))
        if User.objects.filter(id=code).exists():
            break
    return code

# Create your models here.
class User(AbstractUser):
    """ User Model

    Inhireted AbstractUser with addtional parameter for userid.
    """
    class Status_Choices(models.TextChoices):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        DELETED = "DELETED"

    id = models.CharField(unique=True, max_length=16, default=generate_id, primary_key=True, editable=False)
    username = models.CharField(unique=True,null=False, max_length=100)
    status = models.CharField(null=False, choices=Status_Choices.choices, max_length=10, default=Status_Choices.ACTIVE)
    is_superuser = models.BooleanField(default=False)
    first_name = None
    last_name = None
    email = None
    # Will be used for encryption
    # Decryption will be done by private key
    private_key = models.TextField(editable=False, default="")
    # Encryption will be done by public key
    public_key = models.TextField(editable=False, default="")
    # REQUIRED PARAMETER

    user_permissions = None
    groups = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    # Custom Manager
    objects = UserManager()

    def __str__(self) -> str:
        return str(self.username)
    
    # def get_user_by_id(id):
    #     user = User.objects.filter(id=id)
