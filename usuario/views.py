from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
@login_required()
def hello(request):
    #return HttpResponse('Ola Mundo')
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
        #usuarios = Usuario.objects.all()
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

