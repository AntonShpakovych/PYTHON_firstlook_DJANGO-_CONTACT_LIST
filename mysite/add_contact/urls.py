from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from add_contact.views import *


urlpatterns = [
    path('', add_contact, name='add-contact')
]
