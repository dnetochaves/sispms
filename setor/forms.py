from django.forms import ModelForm
from .models import Setor

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['Nome', 'Telefone1', 'Cep', 'Bairro', 'Logradouro', 'Numero', 'Latitude', 'Longitude', 'Gestor', 'Descricao', 'grupo']