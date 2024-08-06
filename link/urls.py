from django.urls import path,include
from .views import *


urlpatterns  = [
   path('create/', create_link, name='create'),
   path('links/',get_user_links,name='links'),
   path('link_delete/',delete_link,name='delete_link'),
   path('health/',health,name='auth')
]