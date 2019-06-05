from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''Our user model that inherits from AbstractUser,
    which give us some already coded functions and 
    other tools'''
    pass