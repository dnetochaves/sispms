from django.db import models
from django.contrib.auth.models import User


class Setor(models.Model):
    Nome = models.CharField(max_length=100)
    Telefone1 = models.CharField(max_length=50)
    Cep = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Logradouro = models.CharField(max_length=50)
    Numero = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Gestor = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=100)
    ##########  ALTERAÇÃO AQUI  ##########
    ##########  'related_name' faz com que você acesse os setores associados a um grupo com grupo.sectors.all()
    grupo = models.ManyToManyField('Grupo', null=True, related_name='sectors')
    ##########  FIM ALTERAÇÃO  ##########
    Codigo = models.CharField('Codigo', max_length=100, null=True, blank=True)
    Email = models.CharField('Email', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Nome


class Grupo(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=50)

    def __str__(self):
        return self.Nome


class Item(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=100)
    SetorItem = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='SetorItem')

    def __str__(self):
        return self.Nome


class Tags(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=50)
    TagSetor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True, related_name='TagSetor')

    def __str__(self):
        return self.Nome


class Status(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.TextField(max_length=500)
    SetoraStatus = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='SetorStatus')

    def __str__(self):
        return self.Nome


class Demandas(models.Model):
    ItemDemanda = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='ItemDemanda')
    Observacao = models.TextField(max_length=2000, null=True, blank=True)
    SetorDemanda = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='SetorDemanda')
    TagsDemandas = models.ManyToManyField('Tags')
    DataRegistro = models.DateTimeField('Data', auto_now_add=True)
    PrazoConclsao = models.DateField('PrazodeConclusão', blank=True, null=True)
    Os = models.CharField(max_length=100, null=True, blank=True)
    StatusDemanda = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, related_name='StatusDemanda')
    UsuarioDemanda = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='UsuarioDemanda')

    def __str__(self):
        return self.Observacao
