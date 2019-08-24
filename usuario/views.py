from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario, Nota
from .forms import UsuarioForm, NotaForm


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
    return render(request, 'usuario/perfil.html')


@login_required()
# TODO: trazer a foto do usuario dinamicamnete
def list_usuario(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        usuarios = Usuario.objects.filter(Nome__contains=busca)
    else:
        usuarios = Usuario.objects.all()

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
# TODO: O campo UsuarioNota não pode ser um campo selecionavel, tem que pegar o usuario logado no sistema
def add_nota(request):
    form = NotaForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/usuario/list_nota')
    return render(request, 'usuario/nota_form.html', {'form': form})


def update_nota(request, id):
    nota = get_object_or_404(Nota, pk=id)
    form = NotaForm(request.POST or None, instance=nota)
    if form.is_valid():
        form.save()
        return redirect('/usuario/list_nota')
    return render(request, 'usuario/nota_form.html', {'form': form})


@login_required()
def list_nota(request):
    busca = request.GET.get('pesquisa', None)
    user = request.user.id

    if busca:
        # usuarios = Usuario.objects.all()
        nota = Nota.objects.filter(Titulo__contains=busca, id=user)
    else:
        nota = Nota.objects.filter(id=user)

    return render(request, 'usuario/list_nota.html', {'nota': nota})


def delete_nota(request, id):
    nota = get_object_or_404(Nota, pk=id)

    if request.method == 'POST':
        nota.delete()
        return redirect('/usuario/list_nota')

    return render(request, 'usuario/nota_delete_confirm.html', {'nota': nota})
