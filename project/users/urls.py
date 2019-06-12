from django.urls import path
from .views import HomePageView, RegisterPageView, LogInPageView, LogOutPageView

urlpatterns=[
    path('', HomePageView.as_view(), name="home"),
    path("register", RegisterPageView.as_view(), name="register"),
    path('login', LogInPageView.as_view(), name="login"),
    path('logout', LogOutPageView.as_view(), name="logout"),
]

