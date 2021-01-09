from django.shortcuts import render, redirect
from .models import Equipamento, Tags
from .forms import EquipamentoForm, TagsForm
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.contrib import messages
from django.db.models import Count, Avg
from django.db.models import Q, Value
from django.db.models.functions import Concat

# Create your views here.


def index(request):
    if not request.user.has_perm('nti.view_equipamento'):
        messages.error(
            request, 'Contate o administrador do sistema. Você não tem permiossão para acessar esse setor')
        return render(request, 'usuario/perfil.html')

    return render(request, 'nti/index.html')


def equipamentos(request):
    eqs = Equipamento.objects.all().order_by('setor')
    total_equipamentos = Equipamento.objects.all().aggregate(
        Count('id'))['id__count']
    return render(request, 'nti/equipamentos.html', {'eqs': eqs, 'total_equipamentos': total_equipamentos})


def add_equipamento(request, equipamento=None):
    #dados_user = Usuario.objects.get(user=request.user.id)
    # return render(request, 'nti/add_equipamentos.html', {'dados_user': dados_user})
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)

        if form.is_valid():
            formulario = form.save()
            formulario.save()
            messages.success(request, 'Equipamento inserido com sucesso')
            return redirect('/nti/equipamentos')
    else:
        form = EquipamentoForm()
        return render(request, 'nti/add_equipamento.html', {'form': form})


def search_equipamento(request, param):
    equipamentos = Equipamento.objects.filter(setor=param)
    total_equipamentos = Equipamento.objects.filter(setor=param).aggregate(
        Count('id'))['id__count']
    return render(request, 'nti/search_equipamento.html', {'equipamentos': equipamentos, 'total_equipamentos': total_equipamentos})


def search(request):
    search = request.GET.get('search')

    if search is None or not search:
        messages.error(request, 'Campo pesquisa não pode ficar vazio')
        return render(request, 'nti/equipamentos.html')

    eqs = Equipamento.objects.filter(

        Q(descricao__icontains=search) |
        Q(fabricante__icontains=search) |
        Q(modelo__icontains=search) |
        Q(tombo__icontains=search) |
        Q(observacao__icontains=search)

    )

    return render(request, 'nti/equipamentos.html', {'eqs': eqs})


def tags(request):
    tags = Tags.objects.all()
    return render(request, 'nti/tags.html', {'tags': tags})


def add_tags(request, tags=None):
    dados_user = Usuario.objects.get(user=request.user.id)
    print(dados_user.SetorUsuario.id)
    if request.method == 'POST':
        form = TagsForm(request.POST, instance=tags)

        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.setor_tag = dados_user.SetorUsuario
            formulario.save()
            messages.success(request, 'Tag inserido com sucesso')
            return redirect('/nti/tags')
    else:
        form = TagsForm()
        return render(request, 'nti/add_tags.html', {'form': form})
