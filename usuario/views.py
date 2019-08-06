from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def hello(request):
    #return HttpResponse('Ola Mundo')
    return render(request, 'index.html')

def list_usuario(request):
    usu = Usuario.objects.all()
    return render(request, 'list_usuario.html', {'usu': usu})

def new_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    return render(request, 'usu_form.html', {'form': form})

def update_usuario(request, id):
    usu = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usu)
    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    return render(request, 'usu_form.html', {'form': form})

def delete_usuario(request, id):
    usu = get_object_or_404(Usuario, pk=id)

    if request.method == 'POST':
        usu.delete()
        return redirect('list_usuario')

    return render(request, 'usu_delete_confirm.html', {'usu': usu})
