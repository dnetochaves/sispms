# Generated by Django 2.2.4 on 2021-02-26 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0014_colaborador_excluido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='colaborador.Cargo'),
        ),
    ]
