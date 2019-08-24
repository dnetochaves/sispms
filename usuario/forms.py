from django.forms import ModelForm
from .models import Usuario, Nota

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nome', 'Email', 'Senha', 'SetorUsuario', 'user', 'photo']


class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = ['Titulo', 'Descricao']