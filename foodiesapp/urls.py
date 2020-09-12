from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('lunch/', views.lunch, name='lunch'),
    path('burger/', views.burger, name='burger'),
    path('kolaches/', views.kolaches, name='kolaches'),
    path('cookies/', views.cookies, name='cookies'),
    path('bread/', views.bread, name='bread'),
    path('gelato/', views.gelato, name='gelato'),
    path('coffee/', views.coffee, name='coffee'),

]