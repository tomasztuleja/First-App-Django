from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse
from .models import CustomUser
from django import forms
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

# Create your views here.

class HomePageView(TemplateView):
    '''Our home page. It is nessessary to redirect Users after register, log in or log out.'''
    template_name = 'project/home.html'


class LogoutRequiredMixin():
    '''Class created to redirect logged in users from register and login pages'''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


class RegisterPageView(LogoutRequiredMixin, CreateView):
    '''Our register page, containing register form from form.py file.'''
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm # Our form from forms.py

    # Redirecting after login
    def get_success_url(self):
        return reverse('home')


class LogInPageView(LogoutRequiredMixin ,auth_views.LoginView):
    '''Our log in page, using form that inherits from Django LoginView.'''
    template_name = "users/login.html"
        
    # Redirecting after login
    def get_success_url(self):
        return reverse('home')


class LogOutPageView(auth_views.LogoutView):
    '''Our log out page, inherited from Django LogoutView, redirected page is defined in settings.py in LOGOUT_REDIRECT_URL variable'''
    pass