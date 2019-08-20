# Generated by Django 2.2.4 on 2019-08-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0002_auto_20190814_1028'),
        ('colaborador', '0003_auto_20190811_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoRemanejamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataRegistro', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('Colaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colaborador_historico', to='colaborador.Colaborador')),
                ('SetorAnterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='setor_anterior_historico', to='setor.Setor')),
                ('SetorAtual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='setor_atual_historico', to='setor.Setor')),
            ],
        ),
    ]
