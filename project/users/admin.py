from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdminDisplay(UserAdmin):
    '''Definning how the display will be look in admin page'''
    add_form = CustomUserCreationForm # Using our forms from forms.py
    model = CustomUser
    list_display = ['email', 'username',] # Atribiutes from CustomUser model which will be displayed in admin page as list

# Register your models here.
admin.site.register(CustomUser, CustomUserAdminDisplay)

