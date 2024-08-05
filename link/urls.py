from django.urls import path,include


def placeholder_view(request):
    pass

urlpatterns  = [
   path('', placeholder_view, name='placeholder'),
]