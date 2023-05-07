from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    print('login')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('userApp:userpg')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('/loginpg/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if cpassword == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('/registerpg/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save
                return redirect('/loginpg/')
        else:
            messages.info(request, 'Password and confirm password should be same')
            return redirect('/registerpg/')

def logout(request):
    auth.logout(request)
    return redirect('homeApp:home')
