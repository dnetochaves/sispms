from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor


# Create your views here.
@login_required()
def painel_setor(request):
    return render(request, 'painel_setor.html')



