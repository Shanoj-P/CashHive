
from django.urls import path
from . import views

app_name = 'userApp'
urlpatterns = [
    path('', views.userpg, name='userpg'),
    path('cardpg/', views.apply, name='cardpg'),
    path('add/', views.add, name='add'),

    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX


]
