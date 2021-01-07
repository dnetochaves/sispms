from django.shortcuts import render, redirect
from .models import Equipamento, Tags
from .forms import EquipamentoForm, TagsForm
from django.contrib.auth.models import User
from usuario.models import Usuario

# Create your views here.


def index(request):
    return render(request, 'nti/index.html')


def equipamentos(request,  equipamento=None):
    eqs = Equipamento.objects.all()
    return render(request, 'nti/equipamentos.html', {'eqs': eqs})


def add_equipamento(request, equipamento=None):
    #dados_user = Usuario.objects.get(user=request.user.id)
    # return render(request, 'nti/add_equipamentos.html', {'dados_user': dados_user})
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)

        if form.is_valid():
            formulario = form.save()
            #formulario.setor = 2
            formulario.save()
            return redirect('/nti/equipamentos')
    else:
        form = EquipamentoForm()
        return render(request, 'nti/add_equipamento.html', {'form': form})


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
            return redirect('/nti/tags')
    else:
        form = TagsForm()
        return render(request, 'nti/add_tags.html', {'form': form})