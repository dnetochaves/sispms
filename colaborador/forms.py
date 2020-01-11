from django.forms import ModelForm
from .models import Colaborador
from .models import Tags
from .models import HistoricoRemanejamento


class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Nome', 'Cpf', 'Telefone', 'tags', 'SetorColaborador', 'ObservacaoExpecificas']

    ##########  ALTERAÇÃO AQUI  ##########
    def __init__(self, tags=None, sectors=None, *args, **kwargs):
        super(ColaboradorForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = tags  ## ISSO SUBSTITUI AS TAGS PADRÃO (ALL) PELO QUE FOI PASSAGO NA FUNÇÃO
        self.fields['SetorColaborador'].queryset = sectors
    ##########  FIM ALTERAÇÃO  ##########


class ColaboradorRemanejamentoForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['SetorColaborador', 'SetorAnterior']
        labels = {'SetorColaborador': 'Setor Atual', 'SetorAnterior': 'Setor Anterior'}

    def __init__(self, sectors=None, *args, **kwargs):
        super(ColaboradorRemanejamentoForm, self).__init__(*args, **kwargs)
        self.fields[
            'SetorColaborador'].queryset = sectors  ## ISSO SUBSTITUI AS TAGS PADRÃO (ALL) PELO QUE FOI PASSAGO NA FUNÇÃO
        self.fields['SetorAnterior'].queryset = sectors


class ObservacaoColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Observacao']

        ##########  ALTERAÇÃO AQUI  ##########
    def __init__(self, tags=None, sectors=None, *args, **kwargs):
        super(ObservacaoColaboradorForm, self).__init__(*args, **kwargs)
        self.fields['Observacao'].queryset = sectors
        ##########  FIM ALTERAÇÃO  ##########


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['Nome', 'Observacao']


class HistoricoRemanejamentoForm(ModelForm):
    class Meta:
        model = HistoricoRemanejamento
        fields = ['ColaboradorHistorico', 'SetorAnterior', 'SetorAtual']
