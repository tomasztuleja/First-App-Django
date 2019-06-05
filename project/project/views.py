from django.urls import path
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    '''Our home page. It is nessessary to redirect Users after register, log in or log out.'''
    template_name = 'project/home.html'


urlpatterns=[
    path('', HomePageView.as_view(), name="home")
]