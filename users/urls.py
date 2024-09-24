from . import views
from django.urls import path

urlpatterns = [
    path('signup' , views.sign_up , name = 'users-sign-up'),
    path('login' , views.login , name = 'users-log-in'),
]