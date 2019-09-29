from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Colaborador, Tags, HistoricoRemanejamento, Setor
from .forms import ColaboradorForm, TagsForm, HistoricoRemanejamentoForm, ColaboradorRemanejamentoForm, \
    ObservacaoColaboradorForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from usuario.models import Usuario
from setor.models import Setor
from django.db.models import Count, Avg


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


@login_required()
def add_colaborador_remanejamento(request):
    form = HistoricoRemanejamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_historico_colaborador.html', {'form': form})


@login_required()
def update_colaborador_remanejamento(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorRemanejamentoForm(request.POST or None, instance=colaborador)

    if form.is_valid():
        form.save()
        if request.method == 'POST':
            setor_id = Colaborador.objects.filter(id=id)
            for setores in setor_id:
                id_setor = setores.SetorColaborador_id
                id_anterior = setores.SetorAnterior_id
            salvar = HistoricoRemanejamento.objects.create(SetorAtual_id=id_setor, SetorAnterior_id=id_anterior,
                                                           ColaboradorHistorico_id=id)
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})


@login_required()
def list_colaborador(request):
    busca = request.GET.get('pesquisa', None)
    if busca:
        col = Colaborador.objects.filter(Nome__contains=busca)
        return render(request, 'colaborador/list_colaborador.html', {'colaborador': col})
    return render(request, 'colaborador/list_colaborador.html')


@login_required()
def list_historico_remanejamento(request, id):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        col = HistoricoRemanejamento.objects.filter(ColaboradorHistorico_id=id)
    else:
        col = HistoricoRemanejamento.objects.filter(ColaboradorHistorico_id=id)

    return render(request, 'colaborador/list_historico_remanejamento.html', {'colaborador': col})


@login_required()
def carta_encaminhamento_colaborador(request, id):
    col = Colaborador.objects.filter(id=id).select_related()

    return render(request, 'colaborador/carta_encaminhamento_colaborador.html', {'colaborador': col})


def update_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})


def observacao_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ObservacaoColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})


@login_required()
def list_setor_colaborador(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        setor = Setor.objects.filter(Nome__contains=busca)
    else:
        setor = Setor.objects.all()

    return render(request, 'colaborador/list_setor.html', {'setor': setor})


@login_required()
def list_colaborador_por_setor(request, id):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        col = Colaborador.objects.filter(Nome__contains=busca)
    else:
        col = Colaborador.objects.filter(SetorColaborador=id)

    return render(request, 'colaborador/list_colaborador.html', {'colaborador': col})


# Functions Tags
@login_required()
def tags_colaborador(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    form = TagsForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.ColaboradorTag_id = id_setor
        form.save()
        return redirect('/colaborador/list_tags')
    return render(request, 'colaborador/add_tags.html', {'form': form})


@login_required()
def list_tags(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    tags = Tags.objects.filter(SetorTag_id=id_setor)
    return render(request, 'colaborador/lista_tags.html', {'tags': tags})


@login_required()
def update_tags(request, id):
    tags = get_object_or_404(Tags, pk=id)
    form = TagsForm(request.POST or None, instance=tags)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_tags')
    return render(request, 'colaborador/add_tags.html', {'form': form})


@login_required()
def info_tags(request, id):
    tags = Colaborador.objects.filter(tags=id)
    qtd_por_tags = Colaborador.objects.filter(tags=id).aggregate(Count('Nome'))['Nome__count']
    desc_tag = Tags.objects.filter(id=id)[0]

    return render(request, 'colaborador/info_tags.html',
                  {'colaborador': tags, 'qtd_por_tags': qtd_por_tags, 'desc_tag': desc_tag})


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
