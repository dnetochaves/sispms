# Generated by Django 2.2.4 on 2019-08-17 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_usuario_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='SetorUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SetorUsuario', to='setor.Setor'),
        ),
    ]