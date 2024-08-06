from django.urls import path,include
from .views import *


urlpatterns  = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('check-auth/', check_auth, name='check_auth'),

]