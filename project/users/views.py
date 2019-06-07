from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse
from .models import CustomUser
from django import forms

# Create your views here.
class RegisterPageView(CreateView):
    '''Our register page, containing register form from form.py file.'''
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('home')
