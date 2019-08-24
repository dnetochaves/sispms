from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor, Grupo
from .forms import SetorForm, GrupoForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
@login_required()
def painel_setor(request):
    return render(request, 'setor/painel_setor.html')


def teste(request):
    setor = Setor.objects.all()

    return render(request, 'setor/list_setor.html', {'setor': setor})


@login_required()
def list_setor(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        setor = Setor.objects.filter(Nome__contains=busca)
    else:
        setor = Setor.objects.all()

    return render(request, 'setor/list_setor.html', {'setor': setor})


@login_required()
def add_setor(request):
    form = SetorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})


@login_required()
def update_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})


# FBV Grupo
@login_required()
def list_grupo(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        grupo = Grupo.objects.filter(Nome__contains=busca)
    else:
        grupo = Grupo.objects.all()

    return render(request, 'setor/list_grupo.html', {'grupo': grupo})


@login_required()
def add_grupo(request):
    form = GrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_grupo')
    return render(request, 'setor/add_grupo.html', {'form': form})


@login_required()
def update_grupo(request, id):
    grupo = get_object_or_404(Grupo, pk=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_grupo')
    return render(request, 'setor/add_grupo.html', {'form': form})


'''
#***Setor CBV***
class ListaSetor(ListView):
    model = Setor

class DetailSetor(DetailView):
    model = Setor

class CreateSetor(CreateView):
    model = Setor
    fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor', 'Descricao', 'grupo']
    success_url = reverse_lazy('setor_list_cbv')

class UpdateSetor(UpdateView):
    model = Setor
    fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor', 'Descricao', 'grupo']
    success_url = reverse_lazy('setor_list_cbv')

#***Grupo CBV****
class ListaGrupo(ListView):
    model = Grupo
    template_name = 'grupo_list.html'

class DetailGrupo(DetailView):
    model = Grupo

class CreateGrupo(CreateView):
    model = Grupo
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('grupo_list_cbv')

class UpdateGrupo(UpdateView):
    model = Grupo
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('grupo_list_cbv')

class DeleteGrupo(DeleteView):
    model = Grupo
    success_url = reverse_lazy('grupo_list_cbv')

'''
