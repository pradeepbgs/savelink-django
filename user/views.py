from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username:
            return JsonResponse({'error':'plss give username'},status=400)
        
        if not email:
            return JsonResponse({'error':'plss give email'},status=400)
        
        if len(password) < 5:
            return JsonResponse({'error':'password must be 5 charcter long'},status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error':'username already exist , try unique username'},
                                status=400)  
              
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error':'email already exist..!!'},
                                status=400)  
        user = User.objects.create_user(
                username=username,
                email=email,
                password=password
        )
        if user:
            return JsonResponse({'message':'user registered successfully'},status=200)
    else :
        return JsonResponse({'error':'method  is not allowd use, POST method'},status=405)
    

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        username = data.get('identifier') or data.get('username')
        password = data.get('password')

        if not username:
            return JsonResponse({'error':'plss give username'},status=400)
        
        if not password:
            return JsonResponse({'error': 'Please provide a password'}, status=400)

        user = authenticate(username=username,password=password)

        if user is not  None:
            login(request,user)
            loggedUser = {
                'username' : user.username,
                'email': user.email
            }
            return  JsonResponse({'message': 'Login successful','user':loggedUser}, status=200)
        else:
            return JsonResponse({'error': "couldn't find user"}, status=401)
        
    else:
        return JsonResponse({'error':'method is not allowed'},status=405)
    

def check_auth(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'isAuthenticated': is_authenticated})