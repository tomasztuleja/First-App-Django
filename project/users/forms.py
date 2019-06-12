from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from project.choices import SEX_CHOICES

class CustomUserCreationForm(UserCreationForm):
    '''Our register form'''

    class Meta:
        '''Defining our form'''
        model = CustomUser # Definig to which model our form should be related
        sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(), required=True)
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", 'sex') # Fields avaliable in our form on register page

    def save(self):
        '''Creating our user and saveing it'''
        custom_user = CustomUser.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], email=self.cleaned_data['email'], sex=self.cleaned_data['sex'])
        custom_user.save()
        return custom_user
