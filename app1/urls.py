from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('kranthi/',kranthi,name='kranthi')
]