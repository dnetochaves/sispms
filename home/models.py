from django.db import models
from setor.models import Setor
from django.contrib.auth.models import User


# Create your models here.
class Feed(models.Model):
    Titulo = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=255)
    SetorFeed = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='SetorFeed')
    UsuarioFeed = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='UsuarioFeed')
    DataRegistro = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return self.Titulo


