from django.shortcuts import render, redirect
from .models import Equipamento, Tags, Historico
from .forms import EquipamentoForm, TagsForm
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.contrib import messages
from django.db.models import Count, Avg
from django.db.models import Q, Value
from django.db.models.functions import Concat
from setor.models import Setor

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


def remanejar_equipamento(request, id):
    equipamento = Equipamento.objects.get(pk=id)
    request.session['id_equipamento_session'] = equipamento.id
    request.session['id_setor_ant_session'] = equipamento.setor.id
    # print(request.session.get('id_setor_ant_session'))

    setores = Setor.objects.all()
    return render(request, 'nti/remanejar_equipamento.html', {'setores': setores, 'equipamento': equipamento})


def finalizar_remanejar_equipamento(request, id):
    id_equipamento_session = request.session.get('id_equipamento_session')
    id_setor_ant_session = request.session.get('id_setor_ant_session')

    equipamento = Equipamento.objects.get(pk=id_equipamento_session)
    equipamento.setor_id = id
    equipamento.save()
    finalizar = Historico.objects.create(
        id_equipamento_id=id_equipamento_session, id_setor_ant_id=id_setor_ant_session, id_setor_atu_id=id)
    
    equipamentos = Equipamento.objects.filter(pk=id_equipamento_session)

    return render(request, 'nti/finalizar_remanejar_equipamento.html', {'equipamentos': equipamentos})


def hitorico(request, id):
    historicos = Historico.objects.filter(id_equipamento_id = id)
    return render(request, 'nti/hitorico.html', {'historicos': historicos})


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
