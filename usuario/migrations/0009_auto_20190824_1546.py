# Generated by Django 2.2.4 on 2019-08-24 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20190824_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='UsuarioNota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsuarioNota', to='usuario.Usuario'),
        ),
    ]
