
from django.urls import path
from . import views

app_name = 'homeApp'
urlpatterns = [
    path('loginpg/', views.loginpg, name='loginpg'),
    path('registerpg/', views.registerpg, name='registrpg'),
    path('', views.home, name='home'),
]
