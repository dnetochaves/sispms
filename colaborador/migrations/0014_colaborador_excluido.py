# Generated by Django 2.2.4 on 2021-01-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0013_colaborador_observacaoexpecificas'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
    ]