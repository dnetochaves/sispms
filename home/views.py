from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home/home.html')

def construction(request):
    return render(request, 'home/construction.html')

def teste_bootstrap(request):
    return render(request, 'home/teste_bootstrap.html')