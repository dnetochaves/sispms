from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Colaborador, Tags
from .forms import ColaboradorForm, TagsForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

@login_required()
def painel_colaborador(request):
    return render(request, 'colaborador/painel_colaborador.html')


# TODO: Refatorado para utilizar CBV remover posteriormente

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


@login_required()
def list_colaborador(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        col = Colaborador.objects.filter(Nome__contains=busca)
    else:
        col = Colaborador.objects.all()

    return render(request, 'colaborador/list_colaborador.html', {'colaborador': col})



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
        # TODO: Resover redirect
        return redirect('/colaborador/lista_tags.html')
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
        # TODO: Resover redirect
        return redirect('/colaborador/lista_tags.html')
    return render(request, 'colaborador/add_tags.html', {'form': form})


'''
# Crud Colaborador CBV
class ListaColaborador(ListView):
    model = Colaborador
    template_name = 'colaborador_list.html'


class DetailColaborador(DetailView):
    model = Colaborador


class CreateColaborador(CreateView):
    model = Colaborador
    fields = ['Nome', 'Cpf',  'Telefone', 'tags', 'SetorColaborador']
    success_url = reverse_lazy('colaborador_list_cbv')


class UpdateColaborador(UpdateView):
    model = Colaborador
    fields = ['Nome', 'Cpf', 'Telefone', 'tags', 'SetorColaborador']
    success_url = reverse_lazy('colaborador_list_cbv')


class DeleteColaborador(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('colaborador_list_cbv')


# Crud Tags CBV
class ListaTags(ListView):
    model = Tags
    template_name = 'tags_list.html'


class DetailTag(DetailView):
    model = Tags


class CreateTag(CreateView):
    model = Tags
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('tag_list_cbv')


class UpdateTag(UpdateView):
    model = Tags
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('tag_list_cbv')

'''