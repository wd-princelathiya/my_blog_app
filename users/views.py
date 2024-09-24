from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


# Create your views here.
def sign_up(request):
    return render(request , 'users/sign_up.html')

def login(request):
    return render(request , 'users/login.html')