from django.shortcuts import render
from django.http import HttpResponse
from main import *
# Create your views here.


def index(request):
    return render(request, 'main/home.html')
