from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')

def teste_bootstrap(request):
    return render(request, 'teste_bootstrap.html')