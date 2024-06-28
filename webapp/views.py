
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User  # or import your custom user model

def user_list(request):
    users = User.objects.all()
    return render(request, 'webapp/user_list.html', {'users': users})
def user_create(request):
    return render(request, 'webapp/user_create.html')
def home_view(request):
    return render(request, 'webapp/home.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'webapp/login.html')

