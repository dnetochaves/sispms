# Generated by Django 2.2.4 on 2019-09-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0014_demandas_usuariodemanda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandas',
            name='UsuarioDemanda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioDemanda', to=settings.AUTH_USER_MODEL),
        ),
    ]
