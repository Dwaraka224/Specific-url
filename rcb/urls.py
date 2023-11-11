from rcb.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('Abd/',Abd,name='Abd'),
]