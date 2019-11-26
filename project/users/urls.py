from django.urls import path, include

from .views import HomePageView, RegisterPageView, LogInPageView, LogOutPageView, EditUserProfilePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('register', RegisterPageView.as_view(), name="register"),
    path('login', LogInPageView.as_view(), name="login"),
    path('logout', LogOutPageView.as_view(), name="logout"),
    path('edit_profile/<str:slug>', EditUserProfilePageView.as_view(), name="edit_profile"),
    path('api-auth/', include('rest_framework.urls')),
]
