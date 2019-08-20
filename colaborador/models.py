from django.core.checks import Tags
from django.db import models
from setor.models import Setor


# Create your models here.
class Colaborador(models.Model):
    Nome = models.CharField(max_length=50)
    Cpf = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')
    SetorColaborador = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='setor')

    def __str__(self):
        return self.Nome


class Tags(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=50)

    def __str__(self):
        return self.Nome


class HistoricoRemanejamento(models.Model):
    ColaboradorHistorico = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='colaborador_historico')
    SetorAnterior = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='setor_anterior_historico')
    SetorAtual = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='setor_atual_historico')
    DataRegistro = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return self.ColaboradorHistorico
