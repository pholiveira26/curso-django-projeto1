from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return render(request, 'SOBRE')

def contato(request):
    return render(request, 'CONTATO')