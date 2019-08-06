from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nome = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Senha = models.CharField(max_length=50)

    def __str__(self):
        return self.Nome