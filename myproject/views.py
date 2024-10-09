from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        # If the user is authenticated, redirect them to the homepage or any other protected page
        return render(request, 'index.html')  # Replace with your homepage template
    else:
        # If not authenticated, redirect to the login page
        return redirect("/api/user/login/")
