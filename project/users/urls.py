from django.urls import path
from .views import HomePageView, RegisterPageView

urlpatterns=[
    path('', HomePageView.as_view(), name="home"),
    path("register", RegisterPageView.as_view(), name="register"),
]

