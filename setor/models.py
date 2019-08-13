from django.db import models

class Setor(models.Model):
    Nome = models.CharField(max_length=50)
    Telefone1 = models.CharField(max_length=50)
    Cep = models.CharField(max_length=50)
    Bairro = models.CharField(max_length=50)
    Logradouro = models.CharField(max_length=50)
    Numero = models.CharField(max_length=50)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Gestor = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome