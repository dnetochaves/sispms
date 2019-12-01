from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor, Grupo, Item, Tags, Demandas, Status
from .forms import SetorForm, GrupoForm, ItemForm, TagForm, DemandaForm, StatusForm
from usuario.models import Usuario
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Avg


# Create your views here.
@login_required()
def painel_setor(request):
    return render(request, 'setor/painel_setor.html')


@login_required()
def painel_demandas(request):
    return render(request, 'setor/painel_demandas.html')


def teste(request):
    setor = Setor.objects.all()

    return render(request, 'setor/list_setor.html', {'setor': setor})


@login_required()
def list_setor(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        setor = Setor.objects.filter(Nome__contains=busca)
    else:
        setor = Setor.objects.all()

    return render(request, 'setor/list_setor.html', {'setor': setor})


@login_required()
def add_setor(request):
    form = SetorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})


@login_required()
def update_setor(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_setor')
    return render(request, 'setor/add_setor.html', {'form': form})


# FBV Grupo
@login_required()
def list_grupo(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        grupo = Grupo.objects.filter(Nome__contains=busca)
    else:
        grupo = Grupo.objects.all()

    return render(request, 'setor/list_grupo.html', {'grupo': grupo})


@login_required()
def add_grupo(request):
    form = GrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_grupo')
    return render(request, 'setor/add_grupo.html', {'form': form})


@login_required()
def update_grupo(request, id):
    grupo = get_object_or_404(Grupo, pk=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_grupo')
    return render(request, 'setor/add_grupo.html', {'form': form})


'''Funções Item'''


@login_required()
def add_item(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    form = ItemForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.SetorItem_id = id_setor
        form.save()
        return redirect('/setor/list_item')
    return render(request, 'setor/add_item.html', {'form': form})


@login_required()
def list_item(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    busca = request.GET.get('pesquisa', None)

    if busca:
        item = Item.objects.filter(SetorItem=id_setor)
    else:
        item = Item.objects.filter(SetorItem=id_setor)

    return render(request, 'setor/list_item.html', {'item': item})


@login_required()
def update_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/setor/list_item')
    return render(request, 'setor/add_item.html', {'form': form})


'''Fim Item'''

'''Funções Tag'''


@login_required()
def list_tag(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    busca = request.GET.get('pesquisa', None)

    if busca:
        tag = Tags.objects.filter(Nome__contains=busca, SetorTag=id_setor)
    else:
        tag = Tags.objects.filter(TagSetor_id=id_setor)
        #tag = Tags.objects.all()

    return render(request, 'setor/list_tag.html', {'tag': tag})


@login_required()
def add_tag(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    form = TagForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.TagSetor_id = id_setor
        form.save()
        return redirect('/setor/list_tag')
    return render(request, 'setor/add_tag.html', {'form': form})


@login_required()
def info_tag(request, id):
    tags = Demandas.objects.filter(TagsDemandas=id)
    qtd_por_tags = Demandas.objects.filter(TagsDemandas=id).aggregate(Count('Observacao'))['Observacao__count']
    desc_tag = Tags.objects.filter(id=id)[0]

    return render(request, 'setor/info_tags.html',
                  {'tags': tags, 'qtd_por_tags': qtd_por_tags, 'desc_tag': desc_tag})


@login_required()
def update_tag(request, id):
    tag = get_object_or_404(Tags, pk=id)

    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.TagSetor_id = id_setor
        form.save()
        return redirect('/setor/list_tag')
    return render(request, 'setor/add_tag.html', {'form': form})


'''Fim Tag'''
'''Funções Demandas'''


@login_required()
def list_demandas(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

        demanda = Demandas.objects.all().order_by('-SetorDemanda')

    return render(request, 'setor/list_demanda.html', {'demanda': demanda})


@login_required()
def list_grupo_setor(request):
    busca = request.GET.get('pesquisa', None)

    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    if busca:
        # usuarios = Usuario.objects.all()
        grupo = Grupo.objects.filter(Nome__contains=busca, setor_id=id_setor)
    else:
        grupo = Grupo.objects.filter(id=id_setor)

    return render(request, 'setor/list_grupo_setor.html', {'grupo': grupo})


@login_required()
def add_demanda(request):
    form = DemandaForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.UsuarioDemanda_id = request.user.id
        form.save()
        return redirect('/setor/list_demandas')
    return render(request, 'setor/add_demanda.html', {'form': form})


@login_required()
def update_demanda(request, id):
    demanda = get_object_or_404(Demandas, pk=id)
    form = DemandaForm(request.POST or None, instance=demanda)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.UsuarioDemanda_id = request.user.id
        form.save()
        return redirect('/setor/list_demandas')
    return render(request, 'setor/add_demanda.html', {'form': form})


'''Fim Demandas'''

'''
Funções Status
'''


@login_required()
def list_status(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

        status = Status.objects.filter(SetoraStatus_id=id_setor)

    return render(request, 'setor/list_status.html', {'status': status})


@login_required()
def info_status(request, id):
    demandas = Demandas.objects.filter(StatusDemanda_id=id)
    qtd_por_tags = Demandas.objects.filter(StatusDemanda_id=id).aggregate(Count('Observacao'))['Observacao__count']
    desc_tag = Status.objects.filter(id=id)[0]
    return render(request, 'setor/info_status.html',
                  {'demandas': demandas, 'qtd_por_tags': qtd_por_tags, 'desc_tag': desc_tag})


@login_required()
def add_status(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    busca_setor = Usuario.objects.filter(user_id=request.user.id)

    for id in busca_setor:
        id_setor = id.SetorUsuario.id

    form = StatusForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.SetoraStatus_id = id_setor
        form.save()
        return redirect('/setor/list_status')
    return render(request, 'setor/add_status.html', {'form': form})


'''
Fim
'''

'''
#***Setor CBV***
class ListaSetor(ListView):
    model = Setor

class DetailSetor(DetailView):
    model = Setor

class CreateSetor(CreateView):
    model = Setor
    fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor', 'Descricao', 'grupo']
    success_url = reverse_lazy('setor_list_cbv')

class UpdateSetor(UpdateView):
    model = Setor
    fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor', 'Descricao', 'grupo']
    success_url = reverse_lazy('setor_list_cbv')

#***Grupo CBV****
class ListaGrupo(ListView):
    model = Grupo
    template_name = 'grupo_list.html'

class DetailGrupo(DetailView):
    model = Grupo

class CreateGrupo(CreateView):
    model = Grupo
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('grupo_list_cbv')

class UpdateGrupo(UpdateView):
    model = Grupo
    fields = ['Nome', 'Observacao']
    success_url = reverse_lazy('grupo_list_cbv')

class DeleteGrupo(DeleteView):
    model = Grupo
    success_url = reverse_lazy('grupo_list_cbv')

'''
