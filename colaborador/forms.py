from django.forms import ModelForm
from .models import Colaborador
from .models import Tags
from .models import HistoricoRemanejamento


class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Nome', 'Cpf', 'Telefone', 'tags', 'SetorColaborador']


class ColaboradorRemanejamentoForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['SetorColaborador', 'SetorAnterior']
        labels = {'SetorColaborador': 'Setor Atual', 'SetorAnterior': 'Setor Anterior'}


class ObservacaoColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Observacao']


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['Nome', 'Observacao']


class HistoricoRemanejamentoForm(ModelForm):
    class Meta:
        model = HistoricoRemanejamento
        fields = ['ColaboradorHistorico', 'SetorAnterior', 'SetorAtual']
