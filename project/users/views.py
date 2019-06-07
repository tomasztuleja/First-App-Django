from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse
from .models import CustomUser
from django import forms
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    '''Our home page. It is nessessary to redirect Users after register, log in or log out.'''
    template_name = 'project/home.html'


class RegisterPageView(CreateView):
    '''Our register page, containing register form from form.py file.'''
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('home')
