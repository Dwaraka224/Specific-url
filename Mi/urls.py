from Mi.views import *
from django.urls import path
app_name='think'
urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bhumra/',bhumra,name='bhumra')
]