# Generated by Django 2.2.4 on 2019-08-11 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0002_colaborador_setorcolaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='SetorColaborador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='setor', to='setor.Setor'),
        ),
    ]
