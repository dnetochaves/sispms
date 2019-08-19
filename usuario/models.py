from django.db import models
from django.contrib.auth.models import User
from setor.models import Setor

# Create your models here.
class Usuario(models.Model):
    Nome = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Senha = models.CharField(max_length=50)
    SetorUsuario = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, related_name='SetorUsuario')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    photo = models.ImageField(upload_to='user_photo', null=True, blank=True)

    def __str__(self):
        return self.Nome