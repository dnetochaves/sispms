from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Colaborador, Tags
from .forms import ColaboradorForm, TagsForm

# Create your views here.
@login_required()
def painel_colaborador(request):
    return render(request, 'colaborador/painel_colaborador.html')

@login_required()
def a4(request):
    return render(request, 'colaborador/a4.html')


@login_required()
def add_colaborador(request):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})

# TODO: Corrigir erro no filtro valor não está chegando na view
@login_required()
def list_colaborador(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        cols = Colaborador.objects.all()
        cols = cols.filter(Nome=busca)
    else:
        cols = Colaborador.objects.all()
    return render(
        request, 'colaborador/list_colaborador.html', {'colaborador': cols})

def update_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})

#Functions Tags
@login_required()
def tags_colaborador(request):
    form = TagsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_tags.html', {'form': form})

@login_required()
def list_tags(request):
    tags = Tags.objects.all()
    return render(request, 'colaborador/lista_tags.html', {'tags': tags})


@login_required()
def update_tags(request, id):
    tags = get_object_or_404(Tags, pk=id)
    form = TagsForm(request.POST or None, instance=tags)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/lista_tags.html')
    return render(request, 'colaborador/add_tags.html', {'form': form})
