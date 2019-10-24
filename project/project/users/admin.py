from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdminDisplay(UserAdmin):
    """Defining how the display will be look in admin page"""
    add_form = CustomUserCreationForm  # Using our forms from forms.py
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', "last_name", 'email', 'username', 'password1', 'password2',)
        }),
    )  # Adding to admin create user page additional fields.
    list_display = ['username', 'email', 'date_joined', "last_name", 'first_name', 'sex']
    # Attributes from CustomUser model which will be displayed in admin page as list


# Register your models here.
admin.site.register(CustomUser, CustomUserAdminDisplay)
