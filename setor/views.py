from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor
from .forms import SetorForm


# Create your views here.
@login_required()
def painel_setor(request):
    return render(request, 'setor/painel_setor.html')

@login_required()
def list_setor(request):
    setor = Setor.objects.all()
    return render(request, 'setor/list_setor.html', {'setor': setor})

@login_required()
def add_setor(request):
    form = SetorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})

def update_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})

