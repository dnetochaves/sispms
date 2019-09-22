from django.forms import ModelForm
from .models import Setor, Grupo, Item, Tags, Demandas, Status


class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor',
                  'Descricao', 'grupo', 'Codigo', 'Email']


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
        fields = ['ItemDemanda', 'Observacao', 'TagsDemandas', 'SetorDemanda', 'PrazoConclsao', 'Os', 'StatusDemanda']
