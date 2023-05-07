from django.http import HttpResponse
from django.shortcuts import render
from .models import District

# Create your views here.
def home(request):
    district = District.objects.all()
    page = 'home'
    return render(request, 'Home.html', {'dist': district, 'page': page})

def loginpg(request):
    district = District.objects.all()
    page = 'login'
    return render(request, 'login.html', {'dist': district, 'page': page})

def registerpg(request):
    district = District.objects.all()
    page = 'register'
    return render(request, 'register.html', {'dist': district, 'page': page})
