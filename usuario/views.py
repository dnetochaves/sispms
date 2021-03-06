from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario, Nota
from .forms import UsuarioForm, NotaForm
from colaborador.models import Colaborador
from colaborador.views import get_accessful_sectors
from django.db.models import Count, Avg
from django.contrib.auth.models import User
from .models import Usuario


# Create your views here.
@login_required()
def hello(request):
    # return HttpResponse('Ola Mundo')
    return render(request, 'usuario/index.html')


def painel_configuracao(request):
    return render(request, 'usuario/painel_configuracao.html')


def painel_usuario(request):
    return render(request, 'usuario/list_usuario.html')


@login_required()
def perfil(request):
    #setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    #a = Colaborador.objects.filter(SetorColaborador_id__in=setores).aggregate(Count('Nome'))['Nome__count']
    #b = Colaborador.objects.all().aggregate(Avg('Nome'))['Nome__avg']
    dados_user = Usuario.objects.get(user=request.user.id)
    return render(request, 'usuario/perfil.html', {'dados_user': dados_user})


@login_required()
# TODO: trazer a foto do usuario dinamicamnete
def list_usuario(request):
    setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        usuarios = Usuario.objects.filter(Nome__contains=busca, SetorUsuario_id__in=setores)
    else:
        usuarios = Usuario.objects.filter(SetorUsuario_id__in=setores)

    return render(request, 'usuario/list_usuario.html', {'usu': usuarios})


@login_required()
def new_usuario(request):
    form = UsuarioForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/usuario/list_usuario')
    return render(request, 'usuario/usu_form.html', {'form': form})


def update_usuario(request, id):
    usu = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usu)
    if form.is_valid():
        form.save()
        return redirect('/usuario/list_usuario')
    return render(request, 'usuario/usu_form.html', {'form': form})


def delete_usuario(request, id):
    usu = get_object_or_404(Usuario, pk=id)

    if request.method == 'POST':
        usu.delete()
        return redirect('usuario/list_usuario')

    return render(request, 'usuario/usu_delete_confirm.html', {'usu': usu})


# Nota
@login_required()
def add_nota(request, nota=None):
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)

        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.UsuarioNota = request.user
            formulario.save()
            return redirect('/usuario/list_nota/')
    else:
        form = NotaForm()
        return render(request, 'usuario/nota_form.html', {'form': form})


def update_nota(request, id):
    nota = get_object_or_404(Nota, pk=id)
    return add_nota(request, nota=nota)


@login_required()
def list_nota(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        nota = Nota.objects.filter(Titulo__contains=busca, UsuarioNota=request.user)
    else:
        nota = Nota.objects.filter(UsuarioNota=request.user)

    return render(request, 'usuario/list_nota.html', {'nota': nota})


def delete_nota(request, id):
    nota = get_object_or_404(Nota, pk=id)

    if request.method == 'POST':
        nota.delete()
        return redirect('/usuario/list_nota')

    return render(request, 'usuario/nota_delete_confirm.html', {'nota': nota})