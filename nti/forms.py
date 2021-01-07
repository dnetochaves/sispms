from django.forms import ModelForm
from .models import Equipamento, Tags


class EquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['descricao', 'fabricante', 'modelo',
                  'tombo', 'observacao', 'setor', 'tag']


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['nome', 'observacao']
