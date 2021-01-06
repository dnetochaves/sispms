from django.db import models
from setor.models import Setor


class Tags(models.Model):
    nome = models.CharField(max_length=50)
    observacao = models.CharField(max_length=50)
    setor_tag = models.ForeignKey(Setor, on_delete=models.CASCADE)


class Equipamento(models.Model):
    descricao = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    tombo = models.CharField(max_length=50, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return self.descricao
