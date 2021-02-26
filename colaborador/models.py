from django.core.checks import Tags
from django.db import models
from setor.models import Setor


class Cargo(models.Model):
    Nome = models.CharField(max_length=50)
    Descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Nome


class Colaborador(models.Model):
    Nome = models.CharField(max_length=50)
    Cpf = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')
    SetorColaborador = models.ForeignKey(
        Setor, on_delete=models.CASCADE, null=True, related_name='setor')
    SetorAnterior = models.ForeignKey(
        Setor, on_delete=models.CASCADE, null=True, related_name='SetorAnterior')
    Observacao = models.TextField(
        max_length=500, null=True, blank=True, help_text='Texto a ser inserido na carta')
    ObservacaoExpecificas = models.TextField(
        max_length=500, null=True, blank=True, help_text='Observações do Colaborador')
    excluido = models.BooleanField(default=False)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Nome


class Tags(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=50)
    SetorTag = models.ForeignKey(
        Setor, on_delete=models.CASCADE, null=True, related_name='SetorTag')

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
        return self.ColaboradorHistorico.id
