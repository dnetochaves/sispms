from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Colaborador, Tags, HistoricoRemanejamento, Setor, Empresa, Cargo
from .forms import ColaboradorForm, TagsForm, HistoricoRemanejamentoForm, ColaboradorRemanejamentoForm, \
    ObservacaoColaboradorForm, RColaboradorForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from usuario.models import Usuario
from setor.models import Setor
from django.db.models import Count, Avg
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.db.models import Q, Value
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
import xlwt
from django.views import View


@login_required()
def painel_colaborador(request):
    # setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    # a = Colaborador.objects.filter(SetorColaborador_id__in=setores, excluido=False).aggregate(
    #    Count('Nome'))['Nome__count']
    a = Colaborador.objects.filter(excluido=False).aggregate(
        Count('Nome'))['Nome__count']
    return render(request, 'colaborador/painel_colaborador.html', {'a': a})


@login_required()
def a4(request):
    return render(request, 'colaborador/a4.html')


##########  ALTERAÇÃO AQUI  ##########
def get_accessful_sectors(sector):
    '''
        Esta função faz com que você obtenha os setores pertencentes aos grupos aos quais um setor está associado
        Você entra com o setor.
    '''
    groups = sector.grupo.all()  # Obtem os grupos associados a um setor
    sectors = []
    for group in groups:
        # Obtem os setores associados a cada grupo
        sectors.extend(group.sectors.all())
    # Retorna todos os setores sem repetição
    return [sector.id for sector in set(sectors)]


##########  FIM ALTERAÇÃO  ##########


@login_required()
def add_colaborador(request, colaborador=None):
    ##########  ALTERAÇÃO AQUI  ##########
    sectors = get_accessful_sectors(request.user.profile.SetorUsuario)
    form = ColaboradorForm(data=request.POST or None, instance=colaborador,
                           sectors=Setor.objects.filter(id__in=sectors), tags=Tags.objects.filter(
                               SetorTag_id__in=sectors))  # Passa só as tags que o colaborador tem permissão
    ##########  FIM ALTERAÇÃO  ##########
    if form.is_valid():
        form.save()
        return redirect('/colaborador/list_colaborador')
    return render(request, 'colaborador/add_colaborador.html', {'form': form})


def update_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    ##########  ALTERAÇÃO AQUI  ##########
    return add_colaborador(request, colaborador=colaborador)
    ##########  FIM ALTERAÇÃO  ##########


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
    sectors = get_accessful_sectors(request.user.profile.SetorUsuario)
    form = ColaboradorRemanejamentoForm(data=request.POST or None, instance=colaborador,
                                        sectors=Setor.objects.filter(id__in=sectors))

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
    if not request.user.has_perm('colaborador.view_colaborador'):
        messages.error(
            request, 'Contate o administrador do sistema. Você não tem permiossão para acessar esse setor')
        return render(request, 'usuario/perfil.html')

    busca = request.GET.get('pesquisa', None)

    ##########  ALTERAÇÃO AQUI  ##########
    setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    if busca:
        col = Colaborador.objects.filter(
            Nome__contains=busca, SetorColaborador_id__in=setores)
        ##########  FIM ALTERAÇÃO  ##########

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
def list_historico(request):
    col = HistoricoRemanejamento.objects.all()
    return render(request, 'colaborador/list_historico.html', {'colaborador': col})


@login_required()
def carta_encaminhamento_colaborador(request, id):
    col = Colaborador.objects.filter(id=id).select_related()
    return render(request, 'colaborador/carta_encaminhamento_colaborador.html', {'colaborador': col})


@login_required()
def observacao_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    ##########  ALTERAÇÃO AQUI  ##########
    sectors = get_accessful_sectors(request.user.profile.SetorUsuario)
    form = ObservacaoColaboradorForm(data=request.POST or None, instance=colaborador,
                                     sectors=Setor.objects.filter(
                                         id__in=sectors))  # Passa só as tags que o colaborador tem permissão
    ##########  FIM ALTERAÇÃO  ##########
    if form.is_valid():
        form.save()
        # TODO PReciso fazer outra função a parte para execultar o bloco da linha 143 a 145 (urgente)
        # carta_encaminhamento_colaborador(request, id)
        col = Colaborador.objects.filter(id=id).select_related()
        return render(request, 'colaborador/carta_encaminhamento_colaborador.html', {'colaborador': col})
    return render(request, 'colaborador/add_colaborador.html', {'form': form})


@login_required()
def list_setor_colaborador(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        setores = get_accessful_sectors(request.user.profile.SetorUsuario)
        # setor = Setor.objects.filter(Nome__contains=busca)
    else:
        setores = get_accessful_sectors(request.user.profile.SetorUsuario)
        # setor = Setor.objects.all()
    ##########  FIM ALTERAÇÃO  ##########
    return render(request, 'colaborador/list_setor.html', {'setor': Setor.objects.filter(id__in=setores)})


@login_required()
def list_colaborador_por_setor(request, id):
    busca = request.GET.get('pesquisa', None)
    ##########  ALTERAÇÃO AQUI  ##########
    setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    if id in setores:

        if busca:
            # usuarios = Usuario.objects.all()
            col = Colaborador.objects.filter(
                Nome__contains=busca, SetorColaborador_id=id)

        else:
            col = Colaborador.objects.filter(SetorColaborador_id=id)
        ##########  FIM ALTERAÇÃO  ##########
        return render(request, 'colaborador/list_colaborador.html', {'colaborador': col})


# Functions Tags
@login_required()
def tags_colaborador(request, tag=None):
    ##########  ALTERAÇÃO AQUI (Melhoramento de código)  ##########
    form = TagsForm(request.POST or None, instance=tag)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.SetorTag_id = request.user.profile.SetorUsuario.id
        ##########  FIM ALTERAÇÃO  ##########
        form.save()
        return redirect('/colaborador/list_tags')
    return render(request, 'colaborador/add_tags.html', {'form': form})


@login_required()
def list_tags(request):
    # TODO: Codigo duplicado melhorar o quanto antes
    ##########  ALTERAÇÃO AQUI  ##########
    setores = get_accessful_sectors(request.user.profile.SetorUsuario)
    tags = Tags.objects.filter(SetorTag_id__in=setores)
    ##########  FIM ALTERAÇÃO  ##########
    return render(request, 'colaborador/lista_tags.html', {'tags': tags})


@login_required()
def update_tags(request, id):
    tag = get_object_or_404(Tags, pk=id)
    return tags_colaborador(request, tag=tag)


@login_required()
def info_tags(request, id):
    tags = Colaborador.objects.filter(tags=id).order_by('-SetorColaborador')
    qtd_por_tags = Colaborador.objects.filter(
        tags=id).aggregate(Count('Nome'))['Nome__count']
    desc_tag = Tags.objects.filter(id=id)[0]

    return render(request, 'colaborador/info_tags.html',
                  {'colaborador': tags, 'qtd_por_tags': qtd_por_tags, 'desc_tag': desc_tag})


# Refatoração
def colaborador(request):
    #colaboradores = Colaborador.objects.filter(excluido=False).order_by('Nome')
    return render(request, 'colaborador/colaborador.html')


def new_colaborador(request):
    form = RColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/colaborador/colaborador')
    return render(request, 'colaborador/new_colaborador.html', {'form': form})


def exclude_colaborador(request, id):
    exc = Colaborador.objects.get(pk=id)
    exc.excluido = True
    exc.save()
    messages.success(
        request, f'O colaborador {exc.Nome} foi alterado com sucesso.')
    return redirect('colaborador')


def edit_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = RColaboradorForm(request.POST or None,
                            request.FILES or None, instance=colaborador)

    if form.is_valid():
        form.save()
        messages.success(
            request, f'O colaborador {colaborador.Nome} foi alterado com sucesso.')
        return redirect('colaborador')
    return render(request, 'colaborador/new_colaborador.html', {'form': form})


def search_colaborador(request):
    search = request.GET.get('search')

    if search is None or not search:
        messages.error(request, 'Campo pesquisa não pode ficar vazio')
        return render(request, 'colaborador/colaborador.html')

    colaboradores = Colaborador.objects.filter(
        Q(Nome__icontains=search) |
        Q(Cpf__icontains=search) |
        Q(Telefone__icontains=search)
    ).filter(excluido=False).order_by('empresa', 'cargo')

    return render(request, 'colaborador/colaborador.html', {'colaboradores': colaboradores})


def remanejar(request, id_colaborador):
    colaborador = Colaborador.objects.get(pk=id_colaborador)
    request.session['id_colaborador_session'] = colaborador.id
    request.session['id_setor_colaborador'] = colaborador.SetorColaborador.id
    # print(request.session.get('id_colaborador_session'))
    # print(request.session.get('id_setor_colaborador'))
    setores = Setor.objects.all()
    return render(request, 'colaborador/remanejar.html', {'setores': setores, 'id_colaborador': colaborador.id, 'id_setor_atu': colaborador.SetorColaborador.id})


def finalizar_remanejar(request, id_setor_atu):
    id_colaborador_session = request.session.get('id_colaborador_session')
    id_setor_colaborador = request.session.get('id_setor_colaborador')

    colaborador_fi = Colaborador.objects.get(pk=id_colaborador_session)
    colaborador_fi.SetorColaborador_id = id_setor_atu
    colaborador_fi.save()

    finalizar = HistoricoRemanejamento.objects.create(
        ColaboradorHistorico_id=id_colaborador_session, SetorAnterior_id=id_setor_colaborador, SetorAtual_id=id_setor_atu)

    messages.success(
        request, f'O colaborador {colaborador_fi.Nome} foi alterado com sucesso.')
    return redirect('/colaborador/colaborador')


def colaborador_setor(request, id):
    colaborador_setors = Colaborador.objects.filter(
        SetorColaborador_id=id, excluido=False).order_by('Nome')
    return render(request, 'colaborador/colaborador.html', {'colaboradores': colaborador_setors})


def setor_colaborador(request):
    setor_colaboradors = Setor.objects.all().order_by('Codigo')
    return render(request, 'colaborador/setor_colaborador.html', {'setor_colaboradors': setor_colaboradors})


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def carta_encaminhamento(request, id):
    template_path = 'colaborador/carta_encaminhamento.html'
    cols = Colaborador.objects.filter(pk=id)
    context = {'cols': cols}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'attachment; filename="carta_encaminhamento.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class rel_geral_colaborador(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="rel_geral_colaborador.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('rel_geral_colaborador')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nome', 'Cpf', 'Telefone', 'SetorColaborador',
                   'Observacao', 'ObservacaoExpecificas', 'cargo', 'empresa']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        cols = Colaborador.objects.filter(excluido=False)

        row_num = 1
        for col in cols:
            ws.write(row_num, 0, col.Nome, font_style)
            ws.write(row_num, 1, col.Cpf, font_style)
            ws.write(row_num, 2, col.Telefone, font_style)
            ws.write(row_num, 3, col.SetorColaborador.Nome, font_style)
            ws.write(row_num, 4, col.Observacao, font_style)
            ws.write(row_num, 5, col.ObservacaoExpecificas, font_style)
            ws.write(row_num, 6, col.cargo.Nome, font_style)
            ws.write(row_num, 7, col.empresa.Nome, font_style)
            row_num += 1

        wb.save(response)
        return response


def table_simples(request):
    col_simples = Colaborador.objects.all()
    return render(request, 'colaborador/table_simples.html', {'col_simples': col_simples})


def historico(request, id):
    historico = HistoricoRemanejamento.objects.filter(
        ColaboradorHistorico_id=id).order_by('DataRegistro')
    return render(request, 'colaborador/historico.html', {'historico': historico})


def tags_colaborador_r(request):
    tags = Tags.objects.all()
    return render(request, 'colaborador/tags.html', {'tags': tags})


def filter_tag(request, id):
    tags_filter = Colaborador.objects.filter(tags=id)
    return render(request, 'colaborador/colaborador.html', {'colaboradores': tags_filter})


def exclude_tag(request, id):
    exc = Tags.objects.get(pk=id)
    exc.delete()
    messages.success(
        request, f'A Tag {exc.Nome} foi excluida com sucesso.')
    return redirect('tags_colaborador')


def list_empresa(request):
    list_empresas = Empresa.objects.all()
    return render(request, 'colaborador/list_empresa.html', {'list_empresas': list_empresas})


def list_empresa_id(request, id):
    request.session['empresa_id'] = id
    list_empresas = Colaborador.objects.filter(
        empresa=id).filter(excluido=False).order_by('cargo').order_by('SetorColaborador')
    return render(request, 'colaborador/list_empresa_id.html', {'list_empresas': list_empresas})


class rel_empresa_colaborador_exclel(View):
    def get(self, request):
        empresa_id = request.session.get('empresa_id')
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="rel_empresa_colaborador_exclel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('rel_empresa_colaborador_exclel')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Nome', 'Cpf', 'Telefone',
                   'SetorColaborador', 'Empresa', 'Cargo']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        cols = Colaborador.objects.filter(
            empresa=empresa_id).filter(excluido=False).order_by('cargo').order_by('SetorColaborador')

        row_num = 1
        for col in cols:
            ws.write(row_num, 0, col.Nome, font_style)
            ws.write(row_num, 1, col.Cpf, font_style)
            ws.write(row_num, 2, col.Telefone, font_style)
            ws.write(row_num, 3, col.SetorColaborador.Nome, font_style)
            ws.write(row_num, 4, col.empresa.Nome, font_style)
            ws.write(row_num, 5, col.cargo.Nome, font_style)
            row_num += 1

        wb.save(response)
        return response
