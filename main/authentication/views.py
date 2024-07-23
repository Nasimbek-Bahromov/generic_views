from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def register_user(request):
    print(request.POST['username'])
    if request.method == 'POST':
        print(request.POST['username'])
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            email= request.POST['email']
        )
        return redirect('login')
    return render(request, 'login-register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index-2')
        else:
            return redirect('error')
    return render(request, 'login-register.html')


def log_out(request):
    logout(request)
    return redirect('index-2')

