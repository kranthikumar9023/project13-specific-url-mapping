from django.urls import path
from app3.views import *
app_name='twothing'
urlpatterns=[
    path('gv/',gv,name='gv'),
]