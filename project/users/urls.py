from django.urls import path
from .views import RegisterPageView

urlpatterns = [
    path("", RegisterPageView.as_view(), name="register"),
]
