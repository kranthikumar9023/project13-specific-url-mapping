from django.urls import path
from app2.views import *
app_name='onething'
urlpatterns=[
    path('giri/',giri,name='giri')
]