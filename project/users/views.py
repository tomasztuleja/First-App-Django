from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, UpdateUserProfileForm
from django.urls import reverse
from .models import CustomUser
from django import forms
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect


# Create your views here.
class HomePageView(TemplateView):
    """Our home page. It is necessary to redirect Users after register, log in or log out."""
    template_name = 'project/home.html'


class LogoutRequiredMixin:
    """Class created to redirect logged in users from register and login pages"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


class RegisterPageView(LogoutRequiredMixin, CreateView):
    """Our register page, containing register form from form.py file."""
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm  # Our form from forms.py

    # Redirecting after login
    def get_success_url(self):
        return reverse('home')


class LogInPageView(LogoutRequiredMixin, auth_views.LoginView):
    """Our log in page, using form that inherits from Django LoginView."""
    template_name = "users/login.html"
        
    # Redirecting after login
    def get_success_url(self):
        return reverse('home')


class LogOutPageView(auth_views.LogoutView):
    """Our log out page, inherited from Django LogoutView,
    redirected page is defined in settings.py in LOGOUT_REDIRECT_URL variable"""
    pass


class EditUserProfilePageView(UpdateView):
    """Our edit profile info which is displaying only profile of the user which is logged in"""
    model = CustomUser
    fields = ['first_name', 'last_name', "sex"]  # Fields which will can be edited
    template_name = 'users/editUserProfile.html'
    slug_field = "username"  # Slug filed which will be in url pattern

    def get_queryset(self):
        """Defining if logged in user can edit profile"""
        user_to_be_edited = CustomUser.objects.filter(username=self.request.user.username)
        # Filtering only objects of the current logged in user, so only logged in users can edit their profile info
        return user_to_be_edited

    def get_success_url(self):
        # Redirecting after login
        return reverse('home')
