from django.forms import ModelForm
from .models import Setor, Grupo, Item, Tags, Demandas, Status


class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor',
                  'Descricao', 'grupo', 'Codigo', 'Email']

    def __init__(self, grupos=None, *args, **kwargs):
        super(SetorForm, self).__init__(*args, **kwargs)
        self.fields['grupo'].queryset = grupos  ## ISSO SUBSTITUI AS TAGS PADRÃO (ALL) PELO QUE FOI PASSAGO NA FUNÇÃO


class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['Nome', 'Observacao']


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['Nome', 'Observacao']


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['Nome', 'Observacao']


class TagForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['Nome', 'Observacao']


class DemandaForm(ModelForm):
    class Meta:
        model = Demandas
        fields = ['ItemDemanda', 'Observacao', 'TagsDemandas', 'PrazoConclsao', 'Os', 'StatusDemanda', 'SetorDemanda']

    def __init__(self, tags=None, status=None, items=None, setores=None, *args, **kwargs):
        super(DemandaForm, self).__init__(*args, **kwargs)
        self.fields['TagsDemandas'].queryset = tags  ## ISSO SUBSTITUI AS TAGS PADRÃO (ALL) PELO QUE FOI PASSAGO NA FUNÇÃO
        self.fields['StatusDemanda'].queryset = status
        self.fields['ItemDemanda'].queryset = items
        self.fields['SetorDemanda'].queryset = setores

