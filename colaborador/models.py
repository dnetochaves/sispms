from django.core.checks import Tags
from django.db import models


# Create your models here.
class Colaborador(models.Model):
    Nome = models.CharField(max_length=50)
    Cpf = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tags')

    def __str__(self):
        return self.Nome


class Tags(models.Model):
    Nome = models.CharField(max_length=50)
    Observacao = models.CharField(max_length=50)

    def __str__(self):
        return self.Nome


from django.db import models

# Create your models here.
