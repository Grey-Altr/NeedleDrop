from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.

# Home view class
class Home(LoginView):
    template_name = 'home.html'