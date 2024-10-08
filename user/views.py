from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get('email')

        if not username:
            return JsonResponse({'success':False,'error':'plss give username'},status=400)
        
        if not email:
            return JsonResponse({'success':False,'error':'plss give email'},status=400)
        
        if len(password) < 5:
            return JsonResponse({'success':False,'error':'password must be 5 charcter long'},status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success':False,'error':'username already exist , try unique username'},
                                status=400)  
              
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success':False,'error':'email already exist..!!'},
                                status=400)  
        user = User.objects.create_user(
                username=username,
                email=email,
                password=password
        )
        if user:
            return JsonResponse({'success':True,'message':'user registered successfully'},status=200)
    else :
        return render(request,'register.html')
    

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username:
            return JsonResponse({'success':False,'error':'plss give username'},status=400)
        
        if not password:
            return JsonResponse({'success':False,'error': 'Please provide a password'}, status=400)

        user = authenticate(username=username,password=password)

        if user is not  None:
            login(request,user)
            loggedUser = {
                'username' : user.username,
                'email': user.email
            }
            return  redirect("/")
        else:
            return JsonResponse({'success':False,'error': "couldn't find user"}, status=401)
        
    else:
        return render(request,'login.html')
    

def check_auth(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'isAuthenticated': is_authenticated})