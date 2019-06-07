from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''Our register form'''
    email = forms.EmailField(required=True) # Creating field that will be avalivale in register page
    first_name = forms.CharField(max_length=50) # Same as above
    last_name = forms.CharField(max_length=50) # Same as above

    class Meta:
        '''Defining our form'''
        model = CustomUser # Definig to which model our form should be related
        fields = ("first_name", "last_name", "username", "email", "password1", "password2") # Fields avaliable in our form on register page

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user