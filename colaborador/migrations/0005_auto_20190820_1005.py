# Generated by Django 2.2.4 on 2019-08-20 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_historicoremanejamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicoremanejamento',
            old_name='Colaborador',
            new_name='ColaboradorHistorico',
        ),
    ]