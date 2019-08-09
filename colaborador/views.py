from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Colaborador
from .forms import ColaboradorForm

# Create your views here.
@login_required()
def painel_colaborador(request):
    return render(request, 'painel_colaborador.html')

@login_required()
def a4(request):
    return render(request, 'a4.html')

@login_required()
def add_colaborador(request):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    return render(request, 'add_colaborador.html', {'form': form})