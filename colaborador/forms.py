from django.forms import ModelForm
from .models import Colaborador
from .models import Tags

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['Nome', 'Cpf', 'Telefone', 'SetorColaborador', 'tags']


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['Nome', 'Observacao']