from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from project.choices import SEX_CHOICES


class CustomUserCreationForm(UserCreationForm):
    """Our register form"""

    class Meta:
        """Defining our form"""
        model = CustomUser  # Defining to which model our form should be related
        sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(), required=True)
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'sex')
        # Fields available in our form on register page

    def save(self):
        """Creating our user and saving it"""
        custom_user = CustomUser.objects.create_user(username=self.cleaned_data['username'],
                                                     password=self.cleaned_data['password1'],
                                                     first_name=self.cleaned_data['first_name'],
                                                     last_name=self.cleaned_data['last_name'],
                                                     email=self.cleaned_data['email'],
                                                     sex=self.cleaned_data['sex']
                                                     )
        custom_user.save()
        return custom_user


class UpdateUserProfileForm(forms.ModelForm):
    """Update profile info form"""
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'sex')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            # Checking if email address is already in use
            raise forms.ValidationError(
                'This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
