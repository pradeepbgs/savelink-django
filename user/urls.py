from django.urls import path,include
from .views import *


urlpatterns  = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),

]