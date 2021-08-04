from django.urls import path
from mysite.views import *
from django.urls.conf import include
from main.views import*


urlpatterns = [
    path('', index, name='home'),
]
