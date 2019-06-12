from django.db import models
from django.contrib.auth.models import AbstractUser
from project.choices import SEX_CHOICES

# Create your models here.
class CustomUser(AbstractUser):
    '''Our user model that inherits from AbstractUser,
    which give us some already coded functions and 
    other tools'''
    email = models.EmailField(unique=True) # AbstractUser have email field, but is not required, so We overwrite it and make it required
    first_name = models.CharField(max_length=50) # Same as above
    last_name = models.CharField(max_length=50) # Same as above
    sex = models.IntegerField(choices=SEX_CHOICES, default=3) # Creating new field that will store user sex